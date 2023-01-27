import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import glob


class ImageGrid:
    def __init__(self, images, rows=4, cols=5):
        self.images = images
        self.rows = rows
        self.cols = cols
        self.total_pages = (len(images) + rows * cols - 1) // (rows * cols)
        self.current_page = 1

        self.root = tk.Tk()
        self.grid_frame = ttk.Frame(self.root)
        self.grid_frame.pack()

        self.create_grid()
        self.create_pagination()
        self.page_label = ttk.Label()

    def create_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                index = i * self.cols + j
                if index >= len(self.images):
                    break
                img = Image.open(self.images[index])
                img = img.resize((100, 100), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                label = ttk.Label(self.grid_frame, image=img)
                label.image = img
                label.grid(row=i, column=j)

    def create_pagination(self):
        pagination_frame = ttk.Frame(self.root)
        pagination_frame.pack()

        prev_button = ttk.Button(
            pagination_frame, text="<", command=self.prev_page)
        prev_button.grid(row=0, column=0)

        self.page_label = ttk.Label(
            pagination_frame, text=f"Page {self.current_page} of {self.total_pages}")
        self.page_label.grid(row=0, column=1)

        next_button = ttk.Button(
            pagination_frame, text=">", command=self.next_page)
        next_button.grid(row=0, column=2)

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.grid_frame.destroy()
            self.grid_frame = ttk.Frame(self.root)
            self.grid_frame.pack()
            self.create_grid()
            self.update_pagination()

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.grid_frame.destroy()
            self.grid_frame = ttk.Frame(self.root)
            self.grid_frame.pack()
            self.create_grid()
            self.update_pagination()

    def update_pagination(self):
        self.page_label.config(
            text=f"Page {self.current_page} of {self.total_pages}")

    def run(self):
        self.root.mainloop()

# Create


images = glob.glob('images/*.jpg')

ig = ImageGrid(images)
ig.run()
