import RPi.GPIO as GPIO

def button_callback(channel):
	print("Button was pressed!")

BUTTONPIN = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTONPIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(BUTTONPIN, GPIO.RISING, callback=button_callback, bouncetime = 300)
try:
	input("Press enter to quit\n\n")

except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()