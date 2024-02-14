import tkinter as tk
from tkinter import Entry  
from Render_image import Image
from Render_Button import Button
from Entry import CustomEntry


screen = tk.Tk()
screen.title("Talk to me!")
primus_canvas = tk.Canvas(screen, width=900, height=600)
primus_canvas.pack()



def render_main_menu():

    background_image = Image(primus_canvas, 0, 0, './assets/bcg_menu.png')
    background_image.draw()

    sign_in_button = Button(primus_canvas, 100, 500, './assets/sign_in_button.png', None)
    sign_in_button.bind('<Button-1>', render_sign_in)

    log_in_button = Button(primus_canvas, 600, 500, './assets/log_in_button.png', None)
    log_in_button.bind('<Button-1>', render_log_in)

    primus_canvas.update()
    screen.mainloop()


def render_sign_in(event=None):

    background_image = Image(primus_canvas, 0, 0, './assets/bcg_signin.png')
    background_image.draw()

    entry1 = CustomEntry(screen, "Username", x=300, y=141)
    entry2 = CustomEntry(screen, "Password", x=300, y=217)
    entry3 = CustomEntry(screen, "Email", x=300, y=293)
    entry4 = CustomEntry(screen, "Confirm email", x=300, y=369)

    sign_in_button = Button(primus_canvas, 330, 450, './assets/sign_in_button.png', None)
    # sign_in_button.bind('<Button-1>', render_sign_in)


    primus_canvas.update()
    screen.mainloop()


def render_log_in(event=None):

    background_image = Image(primus_canvas, 0, 0, './assets/bcg_login.png')
    background_image.draw()

    entry2 = CustomEntry(screen, "Username", x=300, y=217)
    entry3 = CustomEntry(screen, "Password", x=300, y=293)

    log_in_button = Button(primus_canvas, 340, 360, './assets/log_in_button.png', None)
    # log_in_button.bind('<Button-1>', render_sign_in)

    new_here_button = Button(primus_canvas, 269, 430, './assets/new_here_button.png', None)
    new_here_button.bind('<Button-1>', render_sign_in)

    pwd_lost_button = Button(primus_canvas, 430, 430, './assets/pwd_lost_button.png', None)
    # pwd_lost_button.bind('<Button-1>', render_sign_in)

    primus_canvas.update()
    screen.mainloop()



render_main_menu()