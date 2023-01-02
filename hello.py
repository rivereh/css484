# simple program to test tkinter
from tkinter import *
root = Tk()

# create label and pack into root
myLabel = Label(root, text="Hello world!")
myLabel.pack()

# run main loop of root
root.mainloop()