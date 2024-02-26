import tkinter as tk
from tkinter import Label, scrolledtext, simpledialog
from Render.Render_image import Image
from Render.Render_Button import Button
from Render.Entry import CustomEntry
from Authentication import Authentication
from socket_client.Client import Client
import json


screen = tk.Tk()
screen.title("Talk to me!")
primus_canvas = tk.Canvas(screen, width=900, height=600)
primus_canvas.pack()


custom_entries = []
client = Client()
client.connect_to_server('10.10.89.102', 8080)
# client.connect_to_server('127.0.0.1', 8080)
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
    return_authenticate = auth.authenticate(mail, password)
    if return_authenticate[0] == True:
        user = return_authenticate[1]
        render_chat(user)
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


room_button_list = []
room_labels = []


def render_create_room(user, event=None):
    global room_button_list, room_labels
    room_name = simpledialog.askstring("Nouvelle Room", "Entrez le nom de la nouvelle room:")  
    if room_name:
        user.create_room(room_name, user.get_name())
        
        new_room_button = Button(primus_canvas, 20, 100 + 50 * len(room_button_list), './assets/gun_button.png', None)
        new_room_button.bind('<Button-1>', None)
        room_button_list.append(new_room_button)
        
        new_room_label = Label(primus_canvas, text=room_name, bg="black", font=("arial", 15), fg="white")
        new_room_label.place(x=60, y=110 + 40 * len(room_button_list))  
        room_labels.append(new_room_label)

    second_canvas = tk.Canvas(screen, width=630, height=350, bg="lightblue")
    second_canvas.pack(fill=tk.BOTH, expand=True)
    second_canvas.place(x=230, y=100)

    text_area = scrolledtext.ScrolledText(second_canvas, width=56, height=15, font=("Arial", 15), bg="black", fg="white") 
    text_area.insert(tk.INSERT, """\ 
        This is a scrolledtext widget to make tkinter text read only. 
        Hi 
        Geeks !!! 
        Geeks !!! 
        Geeks !!!  
        Geeks !!! 
        Geeks !!! 
        Geeks !!! 
        Geeks !!! 
        Geeks !!! 
        Geeks !!! 
        Geeks !!!  
        Geeks !!! 
        Geeks !!! 
        Geeks !!! 
        Geeks !!! 
        Geeks !!! 
        Geeks !!! 
        Geeks !!!  
        Geeks !!! 
        Geeks !!! 
        Geeks !!! 
        Geeks !!! 
    """) 
    text_area.configure(state ='disabled') 

    new_message = "A new message!"
    text_area.configure(state='normal')
    text_area.insert(tk.END, "\n" + new_message)
    text_area.configure(state='disabled')

    text_area.pack(fill=tk.BOTH, expand=True)


def render_chat(user, event=None):
    global room_button_list, room_labels

    for entry in custom_entries:
        entry.destroy_entry()

    background_image = Image(primus_canvas, 0, 0, './assets/bcg_chat.png')
    background_image.draw()

    micro_button = Button(primus_canvas, 80, 535, './assets/micro_button.png', None)
    # micro_button.bind('<Button-1>', render_chat)
    message_button = Button(primus_canvas, 25, 540, './assets/message_button.png', None)
    # message_button.bind('<Button-1>', render_chat)
    
    setting_button = Button(primus_canvas, 130, 535, './assets/setting_button.png', None)
    # setting_button.bind('<Button-1>', render_main_menu)

    add_chat_button = Button(primus_canvas, 135, 30, './assets/add_chat_button.png', None)
    add_chat_button.bind('<Button-1>', lambda event: render_create_room(user, event))

    delete_button = Button(primus_canvas, 750, 40, './assets/delete_button.png', None)
    # delete_button.bind('<Button-1>', render_main_menu)

    search_button = Button(primus_canvas, 700, 30, './assets/search_button.png', None)
    # search_button.bind('<Button-1>', render_main_menu)

    gun_button = Button(primus_canvas, 820, 500, './assets/gun_button.png', None)
    # gun_button.bind('<Button-1>', render_main_menu)

    room_group_id = user.get_list_room_group()
    room_group_name = user.read_name_room(room_group_id)
    room_group_dict = json.loads(room_group_name)
    print(room_group_dict)

    if isinstance(room_group_dict, dict):
        i = 0  
        for room_name, room_message in room_group_dict.items():

            room_button = Button(primus_canvas, 20, 100 + 50 * i, './assets/gun_button.png', None)
            # room_button.bind('<Button-1>', render_main_menu)
            room_button_list.append(room_button)

            room_label = Label(primus_canvas, text=room_message, bg="black", font=("arial", 15), fg="white")
            room_label.place(x=60, y=110 + 50 * i )  
            room_labels.append(room_label) 
            i += 1

    for button in room_button_list:
        button.bind('<Button-1>', None)

    screen.mainloop()
    primus_canvas.update()