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

# Initialize pins
redPin = 11
greenPin = 13
bluePin = 15
BUTTONPIN = 19

pinOn = GPIO.LOW
pinOff = GPIO.HIGH

counter = 0

# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)
GPIO.setup(BUTTONPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup PWM pins
freq = 60
red = GPIO.PWM(redPin, freq)
green = GPIO.PWM(greenPin, freq)
blue = GPIO.PWM(bluePin, freq)


# Sets all pins to 100% duty cycle (turned off)
def turnAllOff():
	red.start(100)
	green.start(100)
	blue.start(100)


# Callback function changes PWM output based on current counter value
def button_callback(channel):
	global counter, redPin, greenPin, bluePin, pinOn, pinOff
	turnAllOff()
	if counter == 0:
		print("Green")
		green.stop()
		counter += 1
	elif counter == 1:
		print("Yellow")
		green.ChangeDutyCycle(50)
		red.ChangeDutyCycle(50)
		counter += 1
	elif counter == 2:
		print("Red")
		red.stop()
		counter = 0


# Event detector for button press
GPIO.add_event_detect(BUTTONPIN, GPIO.FALLING, callback=button_callback, bouncetime = 300)


# Driver code handles GPIO cleanup and program exit
try:
	input("Press enter to quit\n\n")
	counter = 0
except KeyboardInterrupt:
	pass
finally:
	turnAllOff()
	GPIO.cleanup()
