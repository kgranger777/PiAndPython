# gui4.py
# single LED, two buttons. One to toggle LED, one to quit
# also, one circuit button
#
import RPi.GPIO as GPIO
import tkinter as Tk
import atexit

LEDPIN = 11
BUTTONPIN = 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDPIN,GPIO.OUT)
GPIO.setup(BUTTONPIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def quitter():
	global LEDPIN
	GPIO.output(LEDPIN,GPIO.LOW)
	GPIO.cleanup()

# define toggle function
def toggle():
	global LEDPIN
	GPIO.output(LEDPIN,not(GPIO.input(LEDPIN)))

def buttontoggle(channel):
	toggle()

GPIO.add_event_detect(BUTTONPIN,GPIO.FALLING,callback=buttontoggle,bouncetime=300)

atexit.register(quitter)
root = Tk.Tk()
root.title("My Window")
lbl = Tk.Label(root, text="Use the buttons!")
# Use param sticky=Tk.W+Tk.E+Tk.N
lbl.grid(column=0,columnspan=2)


togglebutton = Tk.Button(root, text="Toggle LED", command=toggle)
togglebutton.grid(row=1, column=0)

quitbtn = Tk.Button(root, text="Exit", command=quit)
quitbtn.grid(row=1, column=1)

root.mainloop()
