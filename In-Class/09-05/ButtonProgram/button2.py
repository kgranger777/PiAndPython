import RPi.GPIO as GPIO

counter = 0

def button_callback(channel):
	global counter
	if counter < 10:
		print("Button was pressed!")
	elif counter < 20:
		print("Okay, that's enough.")
	elif counter < 25:
		print("Stop.")
	elif counter < 28:
		print("...")
	elif counter < 30:
		print("")
	elif counter < 100:
		print("uwu")
	elif counter < 101:
		print("you push all my buttons nyan~")
	else:
		print("bye~")
		quit()

	counter += 1

BUTTONPIN = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTONPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(BUTTONPIN, GPIO.FALLING, callback=button_callback, bouncetime = 300)
try:
	input("Press enter to quit\n\n")
	counter = 0

except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()