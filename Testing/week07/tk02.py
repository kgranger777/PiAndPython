import tkinter as Tk

class Application(Tk.Frame):
	def __init__(self, master=None):
		Tk.Frame.__init__(self, master)
		self.grid()
		self.ltext = Tk.StringVar()
		self.ltext.set("Off")
		self.cbvar = Tk.IntVar()
		self.cbvar.set(0)
		self.createWidgets()

	def change(self):
		if self.cbvar.get() == 1:
			self.ltext.set("On")
		else:
			self.ltext.set("Off")

		# self.ltext.set(("Off","On")[self.cbvar.get()])

	def createWidgets(self):
		self.cbutton = Tk.Checkbutton(self, text="LED", variable=self.cbvar, command=self.change)
		self.cbutton.grid(column=0,columnspan=2)
		self.l1 = Tk.Label(text="LED state: ")
		self.l2 = Tk.Label(textvariable=self.ltext)
		self.l1.grid(row=1,column=0)
		self.l2.grid(row=1,column=1)

def main():
	app = Application()
	app.master.title("My App")
	app.mainloop()

if __name__ == "__main__":
	main()

