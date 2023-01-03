# simple program to test tkinter
from tkinter import *
root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def buttonAdd():
    return

# define buttons
button1 = Button(root, text="1", padx=40, pady=20, command=buttonAdd)
button2 = Button(root, text="2", padx=40, pady=20, command=buttonAdd)
button3 = Button(root, text="3", padx=40, pady=20, command=buttonAdd)
button4 = Button(root, text="4", padx=40, pady=20, command=buttonAdd)
button5 = Button(root, text="5", padx=40, pady=20, command=buttonAdd)
button6 = Button(root, text="6", padx=40, pady=20, command=buttonAdd)
button7 = Button(root, text="7", padx=40, pady=20, command=buttonAdd)
button8 = Button(root, text="8", padx=40, pady=20, command=buttonAdd)
button9 = Button(root, text="9", padx=40, pady=20, command=buttonAdd)
button0 = Button(root, text="0", padx=40, pady=20, command=buttonAdd)
buttonPlus = Button(root, text="+", padx=39, pady=20, command=buttonAdd)
buttonEqual = Button(root, text="=", padx=91, pady=20, command=buttonAdd)
buttonClear = Button(root, text="Clear", padx=79, pady=20, command=buttonAdd)

# put buttons on screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
buttonClear.grid(row=4, column=1, columnspan=2)
buttonPlus.grid(row=5, column=0)
buttonEqual.grid(row=5, column=1, columnspan=2)

# run main loop of root
root.mainloop()