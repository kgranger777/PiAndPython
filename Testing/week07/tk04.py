import tkinter as Tk

class Application(Tk.Frame):
	def __init__(self, master=None):
		Tk.Frame.__init__(self, master)
		self.grid(sticky=Tk.W+Tk.E+Tk.N+Tk.S)
		self.createWidgets()

	def rbCommand(self):
		print(self.rbValue.get())

	def scCommand(self, value):
		print(value, self.scValue.get())

	def getPet(self):
		print("pet = ", self.optionVar.get())

	def createWidgets(self):
		top = self.winfo_toplevel()
		top.columnconfigure(0, weight=1)
		top.rowconfigure(0, weight=1)
		self.label1 = Tk.Label(self, text="Control demo")
		self.label1.grid(columnspan=2)
		self.rbValue = Tk.StringVar()
		self.scValue = Tk.IntVar()
		self.rb1 = Tk.Radiobutton(self, command=self.rbCommand, variable=self.rbValue, text="Cold", value="Too Cold")
		self.rb2 = Tk.Radiobutton(self, command=self.rbCommand, variable=self.rbValue, text="Warm", value="Just Right")
		self.rb3 = Tk.Radiobutton(self, command=self.rbCommand, variable=self.rbValue, text="Hot", value="Too Hot")
		self.rb1.grid(sticky=Tk.W)
		self.rb2.grid(sticky=Tk.W)
		self.rb3.grid(sticky=Tk.W)
		self.rb1.select()
		self.optionVar = Tk.StringVar()
		optionList = ('cat', 'dog', 'fish', 'snek')
		self.optionVar.set(optionList[0])
		self.om = Tk.OptionMenu(self, self.optionVar, *optionList)
		self.om.grid(sticky=Tk.W) 
		self.ombutton = Tk.Button(self, text="Pet", command=self.getPet)
		omrow = int(self.om.grid_info()['row'])
		omcol = int(self.om.grid_info()['column'])
		self.ombutton.grid(row=omrow, column=omcol+1, sticky=Tk.W)
		self.s1 = Tk.Scale(self, orient=Tk.HORIZONTAL, command=self.scCommand, variable=self.scValue)
		self.s1.grid(columnspan=5, sticky=Tk.W+Tk.E+Tk.S)


# configure the rows and columns
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)
		self.columnconfigure(2, weight=1)
		self.columnconfigure(3, weight=1)
		self.columnconfigure(4, weight=1)
		self.rowconfigure(0, weight=1)
		self.rowconfigure(1, weight=0)
		self.rowconfigure(2, weight=0)
		self.rowconfigure(3, weight=0)
		self.rowconfigure(4, weight=0)
		self.rowconfigure(5, weight=1)

def main():
	app = Application()
	app.mainloop()

if __name__ == "__main__":
	main()
