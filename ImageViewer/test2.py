import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import glob


class ImageGrid:
    def __init__(self, images, rows, cols):
        self.images = images
        self.rows = rows
        self.cols = cols
        self.max_page = (len(images) + (rows * cols) - 1) // (rows * cols)
        self.current_page = 1

        self.create_widgets()

    def create_widgets(self):
        self.main_frame = tk.Frame(root)
        self.main_frame.pack()

        self.canvas = tk.Canvas(self.main_frame)
        self.canvas.pack()

        self.images_frame = tk.Frame(self.canvas)
        self.images_frame.pack()

        self.display_images()

        self.pagination_frame = tk.Frame(self.main_frame)
        self.pagination_frame.pack(side='bottom')

        self.prev_button = tk.Button(
            self.pagination_frame, text='Previous', command=self.prev_page)
        self.prev_button.pack(side='left')

        self.page_label = tk.Label(
            self.pagination_frame, text=f'Page {self.current_page} of {self.max_page}')
        self.page_label.pack(side='left')

        self.next_button = tk.Button(
            self.pagination_frame, text='Next', command=self.next_page)
        self.next_button.pack(side='right')

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_pagination()
            self.display_images()

    def next_page(self):
        if self.current_page < self.max_page:
            self.current_page += 1
            self.update_pagination()
            self.display_images()

    def update_pagination(self):
        self.page_label.config(
            text=f'Page {self.current_page} of {self.max_page}')

    def display_images(self):
        for widget in self.images_frame.winfo_children():
            widget.destroy()

        start_index = (self.current_page - 1) * self.rows * self.cols
        end_index = start_index + (self.rows * self.cols)
        current_images = self.images[start_index:end_index]

        for i, image in enumerate(current_images):
            row = i // self.cols
            col = i % self.cols
            img = ImageTk.PhotoImage(Image.open(image))
            label = tk.Label(self.images_frame, image=img)
            label.grid(row=row, column=col)


root = tk.Tk()
root.title("Image Grid")

images = glob.glob('images/*.jpg')

grid = ImageGrid(images, 4, 5)

root.mainloop()
