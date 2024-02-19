import tkinter as tk
from Render.Render_image import Image
from Render.Render_Button import Button
from Render.Entry import CustomEntry
from Authentication import Authentication
from socket_client.Client import Client


screen = tk.Tk()
screen.title("Talk to me!")
primus_canvas = tk.Canvas(screen, width=900, height=600)
primus_canvas.pack()

custom_entries = []
client = Client()
client.connect_to_server('10.10.81.131', 8080)
auth = Authentication(client)

def render_main_menu():

    background_image = Image(primus_canvas, 0, 0, './assets/bcg_menu_2.png')
    background_image.draw()

    sign_in_button = Button(primus_canvas, 100, 500, './assets/sign_in_button.png', None)
    sign_in_button.bind('<Button-1>', lambda event: render_sign_in())

    log_in_button = Button(primus_canvas, 600, 500, './assets/log_in_button.png', None)
    log_in_button.bind('<Button-1>', lambda event: render_log_in())

    screen.mainloop()
    primus_canvas.update()


def on_real_sign_in_button_click(entry1, entry2, entry3, entry4):
    auth.create_account(entry1.get_value(), entry2.get_value(), entry3.get_value(), entry4.get_value())
    render_log_in()

def render_sign_in(event=None):
    background_image = Image(primus_canvas, 0, 0, './assets/bcg_signin.png')
    background_image.draw()

    entry1 = CustomEntry(screen, "Name", x=300, y=141)
    entry2 = CustomEntry(screen, "Username", x=300, y=217)
    entry3 = CustomEntry(screen, "Email", x=300, y=293)
    entry4 = CustomEntry(screen, "Password", x=300, y=369)

    custom_entries.extend([entry1, entry2, entry3, entry4])

    real_sign_in_button = Button(primus_canvas, 330, 450, './assets/sign_in_button_2.png', None)
    real_sign_in_button.bind('<Button-1>', lambda event: on_real_sign_in_button_click(entry1, entry2, entry3, entry4))
    screen.mainloop()
    primus_canvas.update()


    
def check_authenticate(mail, password):
    print("Clicked Log In Button")
    if auth.authenticate(mail, password):
        render_chat()
    else:
        print("Authentication failed")

def render_log_in(event=None):

    for entry in custom_entries:
        entry.destroy_entry()

    background_image = Image(primus_canvas, 0, 0, './assets/bcg_login.png')
    background_image.draw()

    entry5 = CustomEntry(screen, "Email", x=300, y=217)
    entry6 = CustomEntry(screen, "Password", x=300, y=293)

    custom_entries.extend([entry5, entry6])

    real_log_in_button = Button(primus_canvas, 340, 360, './assets/log_in_button_2.png', None)
    real_log_in_button.bind('<Button-1>', lambda event: check_authenticate(entry5.get_value(), entry6.get_value()))



    new_here_button = Button(primus_canvas, 269, 430, './assets/new_here_button.png', None)
    new_here_button.bind('<Button-1>', render_sign_in)

    pwd_lost_button = Button(primus_canvas, 430, 430, './assets/pwd_lost_button.png', None)
    # pwd_lost_button.bind('<Button-1>', render_sign_in)

    screen.mainloop()
    primus_canvas.update()





def render_chat(event=None):

    for entry in custom_entries:
        entry.destroy_entry()

    background_image = Image(primus_canvas, 0, 0, './assets/bcg_chat.png')
    background_image.draw()

    micro_button = Button(primus_canvas, 100, 500, './assets/micro_button.png', None)
    # micro_button.bind('<Button-1>', render_chat)

    add_chat_button = Button(primus_canvas, 600, 500, './assets/add_chat_button.png', None)
    # add_chat_button.bind('<Button-1>', render_main_menu)

    delete_button = Button(primus_canvas, 700, 500, './assets/delete_button.png', None)
    # delete_button.bind('<Button-1>', render_main_menu)

    search_button = Button(primus_canvas, 750, 500, './assets/search_button.png', None)
    # search_button.bind('<Button-1>', render_main_menu)

    setting_button = Button(primus_canvas, 850, 500, './assets/setting_button.png', None)
    # setting_button.bind('<Button-1>', render_main_menu)

    screen.mainloop()
    primus_canvas.update()





