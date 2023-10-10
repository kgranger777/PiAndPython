# tk00a.py
# "your second tkinter program"
# showing the very basics of using tkinter with Python
# this time, with a button!
import tkinter as Tk
root = Tk.Tk()
root.title("My Window")
lbl = Tk.Label(root, text="Click the button below to exit")
lbl.pack()
btn = Tk.Button(root, text="Exit", command=quit)
btn.pack()
root.mainloop()
