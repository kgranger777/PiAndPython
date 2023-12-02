#########
# Name: Kenneth Granger
# Assignment: Programming Assignment 04
# File: granger04.py
# Purpose: Python 3 code sets up GUI and TCP server to change colors of an LED via PWM. The color data is input via
# the GUI and sent to the server by pressing a hardware button.
#
#           NOTE: Works with COMMON ANODE LED (Positive long lead)
#
# Development Computer: Raspberry Pi 4B ARM-v8 64-bit 8GB
# Operating System: Raspbian (Debian) Linux 11 "Bullseye"
# Environment: Python 3.9.2
# IDE: Sublime Text
# Operational status: TODO UPDATE STATUS
#########

# Using the same circuit from assignment 3 (shown below for reference), create a server on port 9000 (NOT a web server)
# that listens for data from a GUI application to control the lights.
# In this case, since you're sending commands, you will need to have a button to send the data to the server.
# Control the colors of the LED like before, toggle the LED, blink the LED (make it blink five times, returning it to
# its previous state before you started blinking. This is actually the easier way to do it.)
# Don't worry about the "Door" button.
# Send the data in whatever format you want, but do not use an HTML server this time.
import tkinter as Tk
from socket import *
from threading import Thread

# Set up pins
redPin = 11
greenPin = 13
bluePin = 15
sendButton = 19

# Set up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)
GPIO.setup(sendButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup PWM pins
freq = 60
red = GPIO.PWM(redPin, freq)
green = GPIO.PWM(greenPin, freq)
blue = GPIO.PWM(bluePin, freq)

# Set initial PWM states
current_pwm = [100, 100, 100]
# Default to a cool white color - mainly used for testing; will be overwritten
last_pwm = [70, 50, 50]


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


# Toggles LED on or off, storing state for restore later
def toggleLED():
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


# # Event detectors for button presses
# GPIO.add_event_detect(powerButton, GPIO.FALLING, callback=updateServer, bouncetime=300)


class Server(Thread):
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        # Buffer size defined as 10k bytes
        self.buffer = 10000
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((self.addr, self.port))
        # Run thread initialization
        Thread.__init__(self)

    def run(self):
        # Backlog size defined as 10k
        self.socket.listen(10000)
        while True:
            client_connection, client_addr = self.socket.accept()
            print("Connected to", str(client_addr[0]) + ":" + str(client_addr[1]))

            message = client_connection.recv(10000)

            # Server should receive messages in the form: message = "("code", data)". Server logic handles hardware
            # updates. If no code received or code in incorrect format, do nothing and continue looping.
            code, data = eval(message.decode())
            print("Server: Received", message.decode(), "[Code", code + ", Data", str(data) + "]")

            # LED update codes received from client:
            if code == 'toggle':
                # Toggle LED state
                toggleLED()
            if code == 'blink':
                # Blink LED 5 times by toggling 10 times
                for _ in range(10):
                    toggleLED()
            if code == 'pwm_r':
                # Update Red PWM
                current_pwm[0] = data
                updateLED()
            if code == 'pwm_g':
                # Update Green PWM
                current_pwm[1] = data
                updateLED()
            if code == 'pwm_b':
                # Update Blue PWM
                current_pwm[2] = data
                updateLED()

            # NOTE shouldn't need to send data from the server, but if I do, here's how to do it...
            # # Test data sending:
            # send_data = data.decode()[::-1]
            # print("Server: Sending", send_data)
            # client_connection.send(send_data.encode())

            # If user wants to quit, close client socket, break out of loop, and shutdown server.
            if code == 'quit':
                client_connection.close()
                break
        self.close()

    # Close socket and turn off LEDs when done
    def close(self):
        print("Shutting down Server")
        turnAllOff()
        GPIO.cleanup()
        self.socket.close()
        return


# class Client:
#     # class Client(Thread):
#     def __init__(self, addr, port):
#         self.addr = addr
#         self.port = port
#         # Buffer size defined as 10k bytes
#         self.buffer = 10000
#         self.socket = socket(AF_INET, SOCK_STREAM)
#         # Thread.__init__(self)
#
#     def send(self):
#         self.socket.connect((self.addr, self.port))
#         # user_input = input("Input a string to be sent")
#         user_input = "This is a test string"
#         # user_input.encode()
#
#         print("Client: Sending", user_input.encode())
#         self.socket.send(user_input.encode())
#
#     def receive(self):
#         # Receive 10k bytes
#         data = self.socket.recv(10000)
#         print("Client: Received", data.decode())
#         self.close()
#
#     # Close socket when done
#     def close(self):
#         print("Shutting down Client")
#         self.socket.close()


# Begin GUI Application class
class Application(Tk.Frame):
    # Initialize red, green, and blue slider variables
    root = Tk.Tk()
    red_value = Tk.IntVar(value=100)
    green_value = Tk.IntVar(value=100)
    blue_value = Tk.IntVar(value=100)

    # Initialize grid and widgets
    def __init__(self, addr, port, master=None):
        # Initialize passed variables
        self.addr = addr
        self.port = port
        # Buffer size defined as 10k bytes
        self.buffer = 10000

        # Set up GUI
        Tk.Frame.__init__(self, master)
        self.grid(sticky='nsew')
        self.createWidgets()

    def send(self, code, data):
        self.socket = socket(AF_INET, SOCK_STREAM)
        # # Connect socket once GUI is set up
        self.socket.connect((self.addr, self.port))

        message = "(\"" + code + "\", " + str(data) + ")"
        print("Client: Sending", message)
        self.socket.send(message.encode())

    # Using internal client socket, send code and current slider value to the server.
    def updateRed(self, event):
        self.send('pwm_r', self.red_value.get())

    def updateGreen(self, event):
        self.send('pwm_g', self.green_value.get())

    def updateBlue(self, event):
        self.send('pwm_b', self.blue_value.get())

    # Send toggle command to server via internal client socket. Sends code only, no data sent.
    def toggleLED(self):
        self.send('toggle', 0)

    # Send blink command to server via socket. No data sent.
    def blinkLED(self):
        self.send('blink', 0)

    # Send quit code to the server and return
    def quit(self):
        self.send('quit', 0)
        self.destroy()
        quit()

    def createWidgets(self):
        self.toggleButton = Tk.Button(self, text="Toggle LED On/Off", command=self.toggleLED)
        self.toggleButton.grid(sticky='ew', padx=(50, 50), pady=(50, 5))

        self.blinkButton = Tk.Button(self, text="Blink LED 5 Times", command=self.blinkLED)
        self.blinkButton.grid(sticky='ew', padx=(50, 50), pady=(5, 5))

        self.redSlider = Tk.Scale(self, from_=100, to=0, orient=Tk.HORIZONTAL, command=self.updateRed,
                                  variable=self.red_value)
        self.redSlider.grid(sticky='ew', padx=(50, 50), pady=(5, 5))

        self.greenSlider = Tk.Scale(self, from_=100, to=0, orient=Tk.HORIZONTAL, command=self.updateGreen,
                                    variable=self.green_value)
        self.greenSlider.grid(sticky='ew', padx=(50, 50), pady=(5, 5))

        self.blueSlider = Tk.Scale(self, from_=100, to=0, orient=Tk.HORIZONTAL, command=self.updateBlue,
                                   variable=self.blue_value)
        self.blueSlider.grid(sticky='ew', padx=(50, 50), pady=(5, 5))

        self.quitButton = Tk.Button(self, text="Quit", command=self.quit)
        self.quitButton.grid(sticky='ew', padx=(50, 50), pady=(5, 10))


def main():
    # Change address and port here
    addr = "localhost"
    port = 9000

    # Sets up threaded instance of server
    th_server = Server(addr, port)
    # Sets up new client application to send data to server from GUI
    app = Application(addr, port)

    # Start server and application
    th_server.start()
    app.mainloop()

    # Wait for server to finish
    th_server.join()


if __name__ == '__main__':
    main()
