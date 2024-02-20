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

user_info = {}
client = Client()
client.connect_to_server('10.10.79.211', 8080)
auth = Authentication(client)

def render_main_menu():

    background_image = Image(primus_canvas, 0, 0, './assets/bcg_menu_2.png')
    background_image.draw()

    sign_in_button = Button(primus_canvas, 100, 500, './assets/sign_in_button.png', None)
    sign_in_button.bind('<Button-1>', lambda event: render_sign_in())

    log_in_button = Button(primus_canvas, 600, 500, './assets/log_in_button.png', None)
    log_in_button.bind('<Button-1>', lambda event: render_log_in())

    primus_canvas.update()
    screen.mainloop()

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

    real_sign_in_button = Button(primus_canvas, 330, 450, './assets/sign_in_button_2.png', None)
    real_sign_in_button.bind('<Button-1>', lambda event: on_real_sign_in_button_click(entry1, entry2, entry3, entry4))

    primus_canvas.update()
    screen.mainloop()

    
def check_authenticate(mail, password):
    print("Clicked Log In Button")
    if auth.authenticate(mail, password):
        render_chat()
    else:
        print("Authentication failed")

def render_log_in(event=None):

    background_image = Image(primus_canvas, 0, 0, './assets/bcg_login.png')
    background_image.draw()

    entry2 = CustomEntry(screen, "Email", x=300, y=217)
    entry3 = CustomEntry(screen, "Password", x=300, y=293)


    real_log_in_button = Button(primus_canvas, 340, 360, './assets/log_in_button_2.png', None)
    real_log_in_button.bind('<Button-1>', lambda event: check_authenticate(entry2.get_value(), entry3.get_value()))

    new_here_button = Button(primus_canvas, 269, 430, './assets/new_here_button.png', None)
    new_here_button.bind('<Button-1>', render_sign_in)

    pwd_lost_button = Button(primus_canvas, 430, 430, './assets/pwd_lost_button.png', None)
    # pwd_lost_button.bind('<Button-1>', render_sign_in)

    primus_canvas.update()
    screen.mainloop()



def render_chat(event=None):

    background_image = Image(primus_canvas, 0, 0, './assets/bcg_chat.png')
    background_image.draw()

    micro_button = Button(primus_canvas, 100, 500, './assets/micro_button.png', None)
    # micro_button.bind('<Button-1>', render_chat)


    primus_canvas.update()
    screen.mainloop()





render_main_menu()