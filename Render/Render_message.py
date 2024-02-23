import tkinter as tk
from tkinter import scrolledtext
import json




class MessageRenderer:
    def __init__(self, screen):
        self.second_canvas = tk.Canvas(screen, width=630, height=350, bg="lightblue")
        self.second_canvas.pack(fill=tk.BOTH, expand=True)
        self.second_canvas.place(x=230, y=100)

        self.text_area = scrolledtext.ScrolledText(self.second_canvas, width=56, height=15, font=("Arial", 15), bg="black", fg="white") 
        self.text_area.configure(state='disabled') 
        self.text_area.pack(fill=tk.BOTH, expand=True)

    def show_message(self, hour, author, message_text):
        params = (hour, author, message_text)
        message = self.client.send_data('READ_TABLE_ROOM', params)
        user_data_json = self.client.receive_data(1024)
        user_data_list = json.loads(user_data_json)

        # Effacez le contenu existant
        self.text_area.configure(state='normal')
        self.text_area.delete(1.0, tk.END)

        for message in user_data_list:
            self.text_area.insert(tk.END, f"{message['author']} ({message['hour']}): {message['message_text']}\n")

        self.text_area.configure(state='disabled')




    
