from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Image viewer')
root.iconbitmap('img/thing.ico')

myImg = ImageTk.PhotoImage(Image.open('img/cs50cat.jpg'))
myLabel = Label(image=myImg)
myLabel.pack()

root.mainloop()