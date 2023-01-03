# simple program to test tkinter
from tkinter import *
root = Tk()

def myClick():
    myLabel = Label(root, text="You clicked the button!")
    myLabel.pack()

myButton = Button(root, text="Click me!", command=myClick)
myButton.pack()

# run main loop of root
root.mainloop()