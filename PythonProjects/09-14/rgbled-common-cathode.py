# rgbled-common-cathode.py - code to test common cathode RGB led
import time
import RPi.GPIO as GPIO

redPin = 11
greenPin = 13
bluePin = 15

pinOn = GPIO.HIGH
pinOff = GPIO.LOW

GPIO.setmode(GPIO.BOARD)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)

def turnAllOff():
	GPIO.output(redPin,pinOff)
	GPIO.output(greenPin,pinOff)
	GPIO.output(bluePin,pinOff)

turnAllOff()

for x in range(100):
	GPIO.output(redPin,pinOn)
	time.sleep(0.016666)
	GPIO.output(redPin,pinOff)
	GPIO.output(greenPin, pinOn)
	time.sleep(0.016666)
	GPIO.output(greenPin, pinOff)
	GPIO.output(bluePin, pinOn)
	time.sleep(0.016666)
	GPIO.output(bluePin, pinOff)

turnAllOff()

GPIO.cleanup()
