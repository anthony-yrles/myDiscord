import tkinter as tk

class Rectangle():
    def __init__(self, canvas, x1, y1, x2, y2, **kwargs):
        self.canvas = canvas
        self.id = None  # Ne crée pas le rectangle immédiatement
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.kwargs = kwargs  # Stocke les paramètres pour redessiner plus tard

    def draw(self):
        """Dessine le rectangle sur le canvas."""
        self.id = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, **self.kwargs)

    def move(self, dx, dy):
        """Déplace le rectangle par la quantité spécifiée dans les directions x et y."""
        self.canvas.move(self.id, dx, dy)
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy

    def delete(self):
        """Supprime le rectangle du canvas."""
        self.canvas.delete(self.id)
