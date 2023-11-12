#########
# Name: Kenneth Granger
# Assignment: Programming Assignment 03
# File: granger03.py
# Purpose: Python 3 code sets up GUI and web server to change colors of 
#           an LED via PWM. The LED is also toggleable via a button and the GUI.
#
#           NOTE: Works with COMMON ANODE LED (Positive long lead)
#
# Development Computer: Raspberry Pi 4B ARM-v8 64-bit 8GB
# Operating System: Raspbian (Debian) Linux 11 "Bullseye"
# Environment: Python 3.9.2
# IDE: Sublime Text
# Operational status: Partially functional - web server does not update
#########
import time
import RPi.GPIO as GPIO
import tkinter as Tk
import http.server, cgi
from os import curdir, sep
from threading import Thread

# Set localhost, port 8000
HOST_NAME = ''
PORT_NUMBER = 8000

# Initialize pins
redPin = 11
greenPin = 13
bluePin = 15
powerButton = 19
sensorButton = 21


# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)
GPIO.setup(powerButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sensorButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup PWM pins
freq = 60
red = GPIO.PWM(redPin, freq)
green = GPIO.PWM(greenPin, freq)
blue = GPIO.PWM(bluePin, freq)

# Set initial PWM states
current_pwm = [100, 100, 100]
# Default to a cool white color - mainly used for testing; will be overwritten
last_pwm = [70, 50, 50]


# Toggles LED on or off, with default channel '0' for GUI button callback
def toggleLED(channel='0'):
	global current_pwm, last_pwm
	if current_pwm[0] < 100 or current_pwm[1] < 100 or current_pwm[2] < 100:
		# Light is on, save state and turn it off
		last_pwm = current_pwm[:]
		current_pwm = [100, 100, 100]
		updateLED()
		print("DEBUG: Turned LED off")
	else:
		# Light is off, reset it back to previous state:
		current_pwm = last_pwm[:]
		updateLED()
		print("DEBUG: Turned LED on")


# Toggle the state of the door
def toggleDoor(channel):
	global app
	print("DEBUG: Door Open")
	while not GPIO.input(channel):
		app.sensorLabel.config(text="The door is open")
	app.sensorLabel.config(text="The door is closed")
	print("DEBUG: Door closed")	


# Cleanup GPIO and server before quitting
def shutdown():
	turnAllOff()
	GPIO.cleanup()
	server.socket.close()
	server.shutdown()
	print("DEBUG: Shutting Down")
	quit()


# Begin HTTP Handler class
class RequestHandler(http.server.BaseHTTPRequestHandler):
	# Handler for GET requests
	def do_GET(self):
		if self.path == "/" or self.path == "/send":
			self.path = "/index.html"
			try:
				sendReply = False
				if self.path.endswith(".html"):
					mimetype = "text/html"
					sendReply = True
				if sendReply:
					f = open(curdir + sep + self.path)
					self.send_response(200)
					self.send_header("Content-type", mimetype)
					self.end_headers()
					self.wfile.write(f.read().encode())
					f.close()
				return
			except IOError:
				self.send_error(404, "File not found: %s" % self.path)

	def do_POST(self):
		if self.path == "/send":
			self.path = "/"
			form = cgi.FieldStorage(
				fp = self.rfile,
				headers = self.headers,
				environ = {"REQUEST_METHOD":"POST",
					"CONTENT-TYPE":self.headers["Content-Type"],
			})

			if form["command"].value == "LED Toggle":
				toggleLED()
			elif form["command"].value == "LED Update":
				print("Updating LED")
				updateLED()

			self.do_GET()
			return


# Begin GUI Application class
class Application(Tk.Frame):
	# Initialize red, green, and blue slider variables
	root = Tk.Tk()
	red_value = Tk.IntVar(value=100)
	green_value = Tk.IntVar(value=100)
	blue_value = Tk.IntVar(value=100)
	
	# Initialize grid and widgets
	def __init__(self, master=None):
		Tk.Frame.__init__(self, master)
		self.grid(sticky='nsew')
		self.createWidgets()

	def updateRed(self, event):
		current_pwm[0] = self.red_value.get()
		updateLED()

	def updateGreen(self, event):
		current_pwm[1] = self.green_value.get()
		updateLED()

	def updateBlue(self, event):
		current_pwm[2] = self.blue_value.get()
		updateLED()


	def createWidgets(self):
		self.toggleButton = Tk.Button(self, text="Toggle LED On/Off", command=toggleLED)
		self.toggleButton.grid(sticky='ew', padx=(50, 50), pady=(50, 5))

		self.redSlider = Tk.Scale(self, from_=100, to=0, orient=Tk.HORIZONTAL, command=self.updateRed, variable=self.red_value)
		self.redSlider.grid(sticky = 'ew', padx=(50, 50), pady=(5,5))

		self.redSlider = Tk.Scale(self, from_=100, to=0, orient=Tk.HORIZONTAL, command=self.updateGreen, variable=self.green_value)
		self.redSlider.grid(sticky = 'ew', padx=(50, 50), pady=(5,5))

		self.redSlider = Tk.Scale(self, from_=100, to=0, orient=Tk.HORIZONTAL, command=self.updateBlue, variable=self.blue_value)
		self.redSlider.grid(sticky = 'ew', padx=(50, 50), pady=(5,5))


		# Label for door sensor status
		self.sensorLabel = Tk.Label(self, text="The door is closed")
		self.sensorLabel.grid(sticky='ew', padx=(50, 50), pady=(5, 5))

		self.quitButton = Tk.Button(self, text="Quit", command=shutdown)
		self.quitButton.grid(sticky='ew', padx=(50, 50), pady=(5, 0))

		
# Initialize app
app = Application()


# Changes duty cycle of PWM pins to value stored in current_pwm list
def updateLED():
	global red, green, blue, current_pwm
	red.ChangeDutyCycle(current_pwm[0])
	green.ChangeDutyCycle(current_pwm[1])
	blue.ChangeDutyCycle(current_pwm[2])


# Turn LED off
def turnAllOff():
	global current_pwm
	current_pwm = [100, 100, 100]
	updateLED()


# Event detectors for button presses
GPIO.add_event_detect(powerButton, GPIO.FALLING, callback=toggleLED, bouncetime=300)
GPIO.add_event_detect(sensorButton, GPIO.FALLING, callback=toggleDoor, bouncetime=300)


# Start the HTTP server
def start_server():
	print("DEBUG: Starting web server")
	server.serve_forever()


# Define server and thread for server
server = http.server.HTTPServer((HOST_NAME, PORT_NUMBER), RequestHandler)
server_thread = Thread(target=start_server)


def main():
	global red, green, blue, app

	# Start PWM pins when program starts
	red.start(100)
	green.start(100)
	blue.start(100)

	# Start web server thread
	server_thread.start()

	# Run application mainloop
	print("DEBUG: Starting application mainloop")
	app.mainloop()


if __name__ == "__main__":
	main()
