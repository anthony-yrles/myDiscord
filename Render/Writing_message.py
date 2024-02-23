import tkinter as tk

class Writing_message:
    def __init__(self, parent, default_text, x, y):
        self.default_text = default_text
        self.max_lines = 10

        self.frame = tk.Frame(parent, bg='black', bd=0, padx=0, pady=0, relief="flat")
        self.frame.place(x=x, y=y)

        self.entry = tk.Text(self.frame, width=47, font=("Arial", ), insertbackground="red", bg="black", fg="white", relief="flat")
        self.entry.insert('1.0', default_text)
        self.entry.bind('<FocusIn>', self.on_entry_click)
        self.entry.pack()

        self.update_size()

    def on_entry_click(self, event):
        if self.entry.get('1.0', 'end-1c') == self.default_text:
            self.entry.delete('1.0', 'end-1c')
            self.entry.config(fg='white')

    def update_size(self):
        self.entry.update_idletasks()
        text_height = self.entry.winfo_reqheight()
        lines = self.entry.get('1.0', 'end-1c').count('\n') + 1
        num_lines = min(lines, self.max_lines)
        self.entry.config(height=num_lines)
        self.frame.config(height=text_height)

    def get_value(self):
        return self.entry.get('1.0', 'end-1c')
    
    def get_frame(self):
        return self.frame

    def destroy_entry(self):
        self.entry.destroy()
        self.frame.destroy()


