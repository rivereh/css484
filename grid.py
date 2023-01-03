# simple program to test tkinter
from tkinter import *
root = Tk()

# create labels
myLabel1 = Label(root, text="Hello world!")
myLabel2 = Label(root, text="My name is River")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

# run main loop of root
root.mainloop()