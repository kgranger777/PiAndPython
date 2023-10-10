import tkinter as Tk

class Application(Tk.Frame):
	def __init__(self, master=None):
		Tk.Frame.__init__(self, master)
		self.grid()
		self.qtext = Tk.StringVar()
		self.qtext.set("Quit")
		self.createWidgets()

	def change(self):
		v = self.qtext.get()
		if v == "Quit":
			self.qtext.set("Exit")
		else:
			self.qtext.set("Quit")

	def createWidgets(self):
		self.changeButton = Tk.Button(self, text="Change", command=self.change)
		self.changeButton.grid(row=0,column=0, sticky=Tk.W)
		self.quitButton = Tk.Button(self, textvariable=self.qtext, command=self.quit)
		self.quitButton.grid(row=0, column=1, sticky=Tk.E)

def main():
	app = Application()
	app.master.title("My App")
	app.mainloop()

if __name__ == "__main__":
	main()

