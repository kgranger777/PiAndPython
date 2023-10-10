# gui3.py
# single LED, two buttons. One to toggle LED, one to quit
#
import RPi.GPIO as GPIO
import tkinter as Tk
import atexit

LEDPIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDPIN,GPIO.OUT)

def quitter():
	global LEDPIN
#	GPIO.output(LEDPIN,GPIO.LOW)
	GPIO.cleanup()

# define toggle function
def toggle():
	global LEDPIN
	GPIO.output(LEDPIN,not(GPIO.input(LEDPIN)))

atexit.register(quitter)
root = Tk.Tk()
root.title("My Window")
lbl = Tk.Label(root, text="Use the buttons!")
lbl.pack()
togglebutton = Tk.Button(root, text="Toggle LED", command=toggle)
togglebutton.pack()
quitbtn = Tk.Button(root, text="Exit", command=quit)
quitbtn.pack()
root.mainloop()
