import tkinter as tk

class Rectangle():
    def __init__(self, canvas, x1, y1, x2, y2, **kwargs):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        self.id = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, **self.kwargs)

    def move(self, dx, dy):
        self.canvas.move(self.id, dx, dy)
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy

    def delete(self):
        self.canvas.delete(self.id)
