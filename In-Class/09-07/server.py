import time
import http.server
import RPi.GPIO as GPIO
from os import curdir, sep

HOST_NAME = ''
PORT_NUMBER = 8000

led_state = GPIO.LOW
LEDPIN = 11

class MyHandler(http.server.BaseHTTPRequestHandler):
	# Handler for GET requests
	def do_GET(sel):
		if self.path == "/" or self.path == "/send":
			self.path = "/demo.html"

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
				self.send_error(404, "File nout found: %s" % self.path)

	def do_POST(self):
		global led_state, LEDPIN
		if self.path == "/send":
			self.path = "/"
			form = cgi.FieldStorage(
				fp = self.rfile,
				headers = self.headers,
				environ = {"REQUEST_METHOD":"POST",
					"CONTENT-TYPE":self.headers["Content-Type"],
			})

			if form["command"].value == "LED":
				print("led_state = ", str(led_state))
				led_state = not led_state
				print("now led_state = ", str(led_state))
				GPIO.output(LEDPIN, led_state)
			elif form["command"].value == "Blink":
				
			self.do_GET()
			return

def main():
	global LEDPIN, led_state, HOST_NAME, PORT_NUMBER
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LEDPIN, GPIO.OUT)

	try:
		server = http.server.BaseHTTPRequestHandler