import tkinter as Tk
from tkinter import LEFT, RIGHT

lblText = "Click button below to quit"
btn1Text = "Quit"
btn2Text = "Be Silly"
root = Tk.Tk()


def silly():
    global lblText, btn1Text, btn2Text, root
    lblText = "SILLY"
    btn1Text = "SILLY"
    btn2Text = "SILLY"
    root.destroy()
    root = Tk.Tk()
    main()


def main():
    global lblText, btn1Text, btn2Text, root
    root.title("My Window")

    lbl = Tk.Label(root, text=lblText)
    lbl.pack()

    buttons = Tk.Frame(root)
    buttons.pack()
    btn1 = Tk.Button(buttons, text=btn1Text, command=quit)
    btn1.pack(side=LEFT)
    btn2 = Tk.Button(buttons, text=btn2Text, command=silly)
    btn2.pack(side=RIGHT)

    root.mainloop()


if __name__ == "__main__":
    main()
