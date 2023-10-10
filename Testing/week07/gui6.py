import tkinter as Tk

class Application(Tk.Frame):
	def __init__(self, master=None):
		Tk.Frame.__init__(self, master)
		self.grid(sticky='nsew')
		self.createWidgets()

	def createWidgets(self):
		self.quitButton = Tk.Button(self, text="Quit", command=self.quit)
		self.quitButton.columnconfigure(0,weight=1)
		self.quitButton.grid(stick='ew')

def main():
	app = Application()
	app.master.title("Sample Application")
	app.mainloop()

if __name__ == "__main__":
	main()
