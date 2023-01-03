# simple program to test tkinter
from tkinter import *
root = Tk()

e = Entry(root, width=25)
e.pack()

def myClick():
    greeting = f'Hello, {e.get()}!'
    myLabel = Label(root, text=greeting)
    myLabel.pack()

myButton = Button(root, text="Enter or name", command=myClick)
myButton.pack()

# run main loop of root
root.mainloop()