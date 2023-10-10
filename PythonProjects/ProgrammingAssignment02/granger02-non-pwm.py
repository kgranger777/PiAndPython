#########
# Name: Kenneth Granger
# Assignment: Programming Assignment 02
# File: granger02.py
# Purpose: Python 3 code responds to button presses and cycles through traffic 
#		   light colors (Green, then Yellow, then Red) repeatedly.
#
#		   NOTE: Works with COMMON ANODE LED (Positive long lead)
#
# Development Computer: Raspberry Pi 4B ARM-v8 64-bit 8GB
# Operating System: Raspbian (Debian) Linux 11 "Bullseye"
# Environment: Python 3.9.2
# IDE: Sublime Text
# Operational status: Functional
#########
import RPi.GPIO as GPIO

redPin = 11
greenPin = 13
bluePin = 15
BUTTONPIN = 19

pinOn = GPIO.LOW
pinOff = GPIO.HIGH

print("counter initialized")
counter = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)
GPIO.setup(BUTTONPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def turnAllOff():
	GPIO.output(redPin, pinOff)
	GPIO.output(greenPin, pinOff)
	GPIO.output(bluePin, pinOff)

def button_callback(channel):
	global counter, redPin, greenPin, bluePin, pinOn, pinOff
	turnAllOff()
	if counter == 0:
		print("Counter is", counter, "showing Green")
		GPIO.output(greenPin, pinOn)
		counter += 1
	elif counter == 1:
		print("Counter is", counter, "showing Yellow")
		GPIO.output([redPin, greenPin], pinOn)
		counter += 1
	elif counter == 2:
		print("Counter is", counter, "showing Red")
		GPIO.output(redPin, pinOn)
		counter = 0



GPIO.add_event_detect(BUTTONPIN, GPIO.FALLING, callback=button_callback, bouncetime = 300)

try:
	input("Press enter to quit\n\n")
	counter = 0

except KeyboardInterrupt:
	pass
finally:
	turnAllOff()
	GPIO.cleanup()

