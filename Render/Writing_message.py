import tkinter as tk
from tkinter import Entry, StringVar

class Writing_message:
    def __init__(self, parent, default_text, x, y):
        self.default_text = default_text


        self.frame = tk.Frame(parent, bg='black', bd=0, padx=0, pady=0)
        self.frame.place(x=x, y=y)

        self.entry_var = StringVar()
        self.text = tk.Text(self.frame, width=57, height=3, font=("Arial", 12), insertbackground="black", bg="black", fg="white", wrap="word", relief="flat")
        self.text.insert(tk.END, default_text)
        self.text.bind('<FocusIn>', self.on_entry_click)
        self.text.pack()

    def on_entry_click(self, event):
        if self.text.get("1.0", "end-1c") == self.default_text:
            self.text.delete("1.0", tk.END)
            self.text.config(fg='white') 

    def get_value(self):
        return self.text.get("1.0", "end-1c")
    
    def get_frame(self):
        return self.frame

    def destroy_entry(self):
        self.text.destroy()
        self.frame.destroy()
