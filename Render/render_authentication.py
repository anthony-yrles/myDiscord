import tkinter as tk
from Render_image import Image
from Render_Button import Button
from Entry import CustomEntry


screen = tk.Tk()
screen.title("Talk to me!")
primus_canvas = tk.Canvas(screen, width=900, height=600)
primus_canvas.pack()

user_info = {}

def render_main_menu():

    background_image = Image(primus_canvas, 0, 0, './assets/bcg_menu_2.png')
    background_image.draw()

    sign_in_button = Button(primus_canvas, 100, 500, './assets/sign_in_button.png', None)
    sign_in_button.bind('<Button-1>', lambda event: render_sign_in())

    log_in_button = Button(primus_canvas, 600, 500, './assets/log_in_button.png', None)
    log_in_button.bind('<Button-1>', lambda event: render_log_in())

    primus_canvas.update()
    screen.mainloop()


def render_sign_in(event=None):
    background_image = Image(primus_canvas, 0, 0, './assets/bcg_signin.png')
    background_image.draw()

    entry1 = CustomEntry(screen, "Username", x=300, y=141)
    entry2 = CustomEntry(screen, "Password", x=300, y=217)
    entry3 = CustomEntry(screen, "Email", x=300, y=293)
    entry4 = CustomEntry(screen, "Confirm email", x=300, y=369)

    real_sign_in_button = Button(primus_canvas, 330, 450, './assets/sign_in_button_2.png', None)
    real_sign_in_button.bind('<Button-1>', lambda event: check_sign_in(entry1, entry2, entry3, entry4))

    primus_canvas.update()
    screen.mainloop()

    

def check_sign_in(entry1, entry2, entry3, entry4):
    
    entry_values = {
        "Username": entry1.get_value(),
        "Password": entry2.get_value(),
        "Email": entry3.get_value(),
        "Confirm_email": entry4.get_value(),
    }

    print("Clicked Sign In Button")
    print("Entry Values:", entry_values)

    if all(value != "" and value != entry.default_text for value, entry in zip(entry_values.values(), [entry1, entry2, entry3, entry4])):
        user_info["sign_in"] = entry_values
        print("User Info:", user_info["sign_in"])


def render_log_in(event=None):

    background_image = Image(primus_canvas, 0, 0, './assets/bcg_login.png')
    background_image.draw()

    entry2 = CustomEntry(screen, "Username", x=300, y=217)
    entry3 = CustomEntry(screen, "Password", x=300, y=293)

    entry_values = {
        "Username": entry2.get_value(),
        "Password": entry3.get_value(),
    }

    user_info["log_in"] = entry_values

    log_in_button = Button(primus_canvas, 340, 360, './assets/log_in_button.png', None)
    log_in_button.bind('<Button-1>', render_chat)

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