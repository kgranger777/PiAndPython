# program to blink LED - simple sample
import time
import RPi.GPIO as GPIO
# Set the LED pin number
LEDPIN = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDPIN, GPIO.OUT)

for i in range(20):
	print("High")
	GPIO.output(LEDPIN, GPIO.HIGH)
	time.sleep(0.5)
	print("Low")
	GPIO.output(LEDPIN, GPIO.LOW)
	time.sleep(0.5)

GPIO.cleanup()
