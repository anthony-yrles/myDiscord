import tkinter as tk
from Render_image import Image
from Render_Button import Button
from Entry import CustomEntry
from Authentication import Authentication
from socket_client.Client import Client
import json


def render_create_message(event=None):

    # for entry in writing_message:
    #     entry.destroy_frame()

    # background_image = Image(primus_canvas, 0, 0, './assets/bcg_create_message.png')
    # background_image.draw()

    enter_text = Writing_message(screen, "Write your message", x=260, y=491)    
    custom_entries.append(enter_text)

    gun_button = Button(primus_canvas, 820, 500, './assets/gun_button.png', None)
    

    screen.mainloop()
    primus_canvas.update()








    
