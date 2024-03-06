import tkinter as tk

class Image():
    def __init__(self, canvas, x, y, image_path):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.image = tk.PhotoImage(file=image_path) 
        self.image_id = self.canvas.create_image(self.x, self.y, image=self.image, anchor=tk.NW)

    def draw(self):
        if self.canvas.winfo_exists():
            self.canvas.create_image(self.x, self.y, image=self.image, anchor=tk.NW)

    def move(self, x, y):
        self.x = x
        self.y = y
        self.canvas.coords(self.image_id, self.x, self.y)

    def delete(self):
        self.canvas.delete(self.image_id)

    def get_position(self):
        return self.x, self.y

    def get_size(self):
        return self.image.width(), self.image.height()