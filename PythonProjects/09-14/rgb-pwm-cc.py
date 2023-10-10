# rgb-pwm-cc.py PWM with Common Cathode RGB LED
import RPi.GPIO as GPIO
import time

REDPIN = 11
GREENPIN = 13
BLUEPIN = 15

def main():
	RUNNING = True

	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(REDPIN, GPIO.OUT)
	GPIO.setup(GREENPIN, GPIO.OUT)
	GPIO.setup(BLUEPIN, GPIO.OUT)

	freq = 120

	# setup my PWM objects
	red = GPIO.PWM(REDPIN, freq)
	green = GPIO.PWM(GREENPIN, freq)
	blue = GPIO.PWM(BLUEPIN, freq)

	try:
		# note normal values - 100 = on
		red.start(100)
		green.start(0)
		blue.start(0)

		time.sleep(1)

		for i in range(0,101):
			green.ChangeDutyCycle(i)
			blue.ChangeDutyCycle(i)
			red.ChangeDutyCycle(100 - i)
			time.sleep(0.15)

	except Exception as e:
		print(e)
		RUNNING = False
	finally:
		red.stop()
		green.stop()
		blue.stop()
		GPIO.cleanup()

if __name__ == "__main__":
	main()
