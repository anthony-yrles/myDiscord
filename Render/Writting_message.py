import tkinter as tk

class Writting_message:
    def __init__(self, parent, default_text, x, y):
        self.default_text = default_text
        self.max_lines = 10

        self.frame = tk.Frame(parent, bg='black', bd=0, padx=0, pady=0, relief="flat")
        self.frame.place(x=x, y=y)

        self.entry = tk.Text(self.frame, width=33, font=("Arial", 20), insertbackground="red", bg="black", fg="white", relief="flat")
        self.entry.insert('1.0', default_text)
        self.entry.bind('<FocusIn>', self.on_entry_click)
        self.entry.bind('<Key>', self.on_key_press)
        self.entry.pack()

    def on_entry_click(self, event):
        if self.entry.get('1.0', 'end-1c') == self.default_text:
            self.entry.delete('1.0', 'end-1c')
            self.entry.config(fg='white') 

    def on_key_press(self, event):
        lines = self.entry.get('1.0', 'end-1c').split('\n')
        num_lines = min(len(lines), self.max_lines)
        self.entry.config(height=num_lines)

    def get_value(self):
        return self.entry.get('1.0', 'end-1c')
    
    def get_frame(self):
        return self.frame

    def destroy_entry(self):
        self.entry.destroy()
        self.frame.destroy()


