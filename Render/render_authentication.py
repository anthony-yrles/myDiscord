import tkinter as tk
import threading
from tkinter import Label, scrolledtext, simpledialog
from Render.Render_image import Image
from Render.Render_Button import Button
from Render.Entry import CustomEntry
from Render.Writing_message import Writing_message
from Render.list_room import list_room
from Authentication import Authentication
from Private import Private
from socket_client.Client import Client
from Vocal_message import Vocal_Recorder

screen = tk.Tk()
screen.title("Talk to me!")
primus_canvas = tk.Canvas(screen, width=900, height=600)
primus_canvas.pack()

custom_entries = []
area_message = []
message_entry = [] 
received_messages = []
displayed_messages = []
room_button_list = []
room_labels = []
client = Client()
auth = Authentication(client)
second_canvas = None
text_area = None

run = False
update_event = threading.Event()
text_area_lock = threading.Lock()

def read_messages_loop():
    while run:
        data = client.receive_data(1024)
        if data :
            received_messages.append(data)
    update_event.set()

def render_main_menu():

    for entry in custom_entries:
        entry.destroy_entry()
    for enter_text in area_message:
        enter_text.destroy_entry()
    for label in room_labels:
        label.destroy()
        

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
    return_authenticate = auth.authenticate(mail, password)
    if return_authenticate[0] == True:
        user = return_authenticate[1]
        
        client.connect_to_server('127.0.0.1', 8080)
        threading.Thread(target=read_messages_loop).start()
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

    screen.mainloop()
    primus_canvas.update()

def render_message_send(user, id_room, gun_button, event=None):
    global second_canvas, text_area

    if second_canvas is None:
        second_canvas = tk.Canvas(screen, width=630, height=350, bg="lightblue")
        second_canvas.pack(fill=tk.BOTH, expand=True)
        second_canvas.place(x=230, y=100)
    else :
        for widget in second_canvas.winfo_children():
            widget.destroy()
        
    text_area = scrolledtext.ScrolledText(second_canvas, width=56, height=15, font=("Arial", 15), bg="black", fg="white", relief=tk.FLAT)
    
    gun_button.bind('<Button-1>', lambda event=None, user=user, id_room=id_room: send_message(user, id_room, event))

    messages, room_ids = user.read_message()
    
    dates = []
    authors = []
    texts = []

    dates = [message[0] for message in messages]
    authors = [message[1] for message in messages]
    texts = [message[2] for message in messages]

    for messages, date, author, text, room_id in zip(messages, dates, authors, texts, room_ids):
        if room_id == id_room:
            text_area.insert(tk.INSERT, f"Date: {date}\nAuteur: {author}\nMessage: {text.replace('{', '').replace('}', '')}\n\n")

    text_area.configure(state ='disabled') 
    text_area.pack(fill=tk.BOTH, expand=True)

def refresh_messages(text_area):
    global received_messages, displayed_messages
    if run:
        update_event.wait()
        with text_area_lock:
            text_area.configure(state='normal')
            for message in received_messages:
                if message not in displayed_messages:
                    text_area.insert(tk.END, message + '\n')
                    displayed_messages.append(message)
                    text_area.configure(state='disabled')

        received_messages = []
        update_event.clear()

def render_create_room(user, event=None):
    global room_button_list, room_labels
    room_name = simpledialog.askstring("Nouvelle Room", "Entrez le nom de la nouvelle room:")  
    if room_name:
        user.create_room(room_name, user.get_name())

def render_create_message(user, event=None):
    enter_text = Writing_message(screen, "", x=260, y=491)    
    message_entry.append([enter_text])
    area_message.extend([enter_text])
    enter_text.set_value("")

def send_message(user, id_room, event=None):
    global received_messages
    author = user.get_name()
    message_text = message_entry[0][0].get_value()
    try:
        user.create_message(author, message_text, id_room)
        message_entry[0][0].set_value("")
    except Exception as e:
        print(f"Error sending message: {e}")
  

def render_chat(user, event=None):
    global room_button_list, room_labels
    type_room = 'text_room'
    
    for entry in custom_entries:
        entry.destroy_entry()
    for label in room_labels:
        label.destroy()


    background_image = Image(primus_canvas, 0, 0, './assets/bcg_chat.png')
    background_image.draw()
 
    render_create_message(user)

    micro_button = Button(primus_canvas, 80, 535, './assets/micro_button.png', None)
    micro_button.bind('<Button-1>', lambda event: render_vocal_chat(user, event))

    setting_button = Button(primus_canvas, 135, 535, './assets/setting_button.png', None)
    setting_button.bind('<Button-1>', lambda event: render_private_chat(user, event))

    message_button = Button(primus_canvas, 25, 540, './assets/message_button.png', None)
    message_button.bind('<Button-1>', lambda event: render_chat(user, event))

    add_chat_button = Button(primus_canvas, 135, 30, './assets/add_chat_button.png', None)
    add_chat_button.bind('<Button-1>', lambda event: render_create_room(user, event))

    delete_button = Button(primus_canvas, 750, 40, './assets/delete_button.png', None)
    delete_button.bind('<Button-1>', lambda event: render_main_menu())

    gun_button = Button(primus_canvas, 820, 500, './assets/gun_button.png', None)

    room_button_list, room_id_list = list_room(primus_canvas, user, room_button_list, room_labels, type_room,  client.client_socket)

    for button, id_room in zip(room_button_list, room_id_list):
        button.bind('<Button-1>', lambda event, id=id_room: render_message_send(user, id, gun_button, event))

    screen.mainloop()
    primus_canvas.update()

vocal_room_button_list = []
vocal_room_id_list = []
listen_button_list = []

def render_vocal_chat(user, event=None):
    global room_labels, area_message, vocal_room_button_list, vocal_room_id_list
    type_room = 'vocal_room'

    for enter_text in area_message:
        enter_text.destroy_entry()

    for label in room_labels:
        label.destroy()

    background_vocal = Image(primus_canvas, 0, 0, './assets/bcg_chat.png')
    background_vocal.draw()

    micro_button2 = Button(primus_canvas, 80, 535, './assets/micro_button2.png', None)
    micro_button2.bind('<Button-1>', lambda event: render_vocal_chat(user, event))

    setting2_button = Button(primus_canvas, 135, 535, './assets/setting_button2.png', None)
    setting2_button.bind('<Button-1>', lambda event: render_private_chat(user, event))
   
    message_button2 = Button(primus_canvas, 25, 540, './assets/message_button2.png', None)
    message_button2.bind('<Button-1>', lambda event: render_chat(user, event))

    add_chat_button2 = Button(primus_canvas, 135, 30, './assets/add_chat_button2.png', None)
    add_chat_button2.bind('<Button-1>', lambda event: render_create_vocal_room(user, event))

    delete_button2 = Button(primus_canvas, 750, 40, './assets/delete_button2.png', None)
    delete_button2.bind('<Button-1>', lambda event: render_main_menu())
    if delete_button2.bind('<Button-1>', lambda event: render_main_menu()):
        for label in room_labels:
            label.destroy()

    gun_button2 = Button(primus_canvas, 820, 500, './assets/gun_button2.png', None)

    vocal_room_button_list, vocal_room_id_list = list_room(primus_canvas, user, vocal_room_button_list, room_labels, type_room, client.client_socket)

    for button, id_room in zip(vocal_room_button_list, vocal_room_id_list):
        button.bind('<Button-1>', lambda event, id=id_room: render_vocal_send(user, id, gun_button2, event))

    screen.mainloop()
    primus_canvas.update()

def render_create_vocal_room(user, event=None):
    global room_button_list, room_labels
    room_name = simpledialog.askstring("Nouvelle Room", "Entrez le nom de la nouvelle room:")  
    if room_name:
        user.create_vocals_rooms(room_name, user.get_name())

def render_vocal_send(user, id_room, gun_button, event=None):
    global primus_canvas, second_canvas, text_area, listen_button_list
    listen_button_list.clear()

    if second_canvas is None:
        second_canvas = tk.Canvas(screen, width=630, height=350, bg="lightblue")
        second_canvas.pack(fill=tk.BOTH, expand=True)
        second_canvas.place(x=290, y=100)
    else :
        for widget in second_canvas.winfo_children():
            widget.destroy()

    recorder = Vocal_Recorder()

    gun_button.bind('<Button-1>', lambda event: recorder.start_recording(user))
    text_area = scrolledtext.ScrolledText(second_canvas, width=50, height=15, font=("Arial", 15), bg="black", fg="white",relief=tk.FLAT) 

    messages, room_ids = user.listen_message_room_ids()
    
    dates = []
    authors = []

    dates = [message[0] for message in messages]
    authors = [message[1] for message in messages]
    i = 0
    for message, date, author in zip(messages, dates, authors):
        if message[3] == id_room:
            listen_button = Button(primus_canvas, 245, 120 + 92 * i, './assets/listen_button.png', None)
            listen_button_list.append(listen_button)

            message_text = f"Date: {date}\nAuteur: {author}\nMessage:{'Vous a envoyé un message vocal'}\n\n"
            text_area.insert(tk.END, message_text)
            
            i+=1
    for i, button in enumerate(listen_button_list):
        button.bind('<Button-1>', lambda event, index=i: user.listen_message(index))

    text_area.configure(state ='disabled') 
    text_area.pack(fill=tk.BOTH, expand=True)

    screen.mainloop()
    second_canvas.update()

user_list_button = []
user_label_list = []

def render_private_chat(user, event=None):
    global room_labels, area_message
    private = Private(client)

    for label in room_labels:
        label.destroy()

    background_vocal = Image(primus_canvas, 0, 0, './assets/bcg_chat.png')
    background_vocal.draw()

    micro_button3 = Button(primus_canvas, 80, 535, './assets/micro_button3.png', None)
    micro_button3.bind('<Button-1>', lambda event: render_vocal_chat(user, event))

    setting3_button = Button(primus_canvas, 135, 535, './assets/setting_button3.png', None)
    setting3_button.bind('<Button-1>', lambda event: render_private_chat(user, event))
   
    message_button3 = Button(primus_canvas, 25, 540, './assets/message_button3.png', None)
    message_button3.bind('<Button-1>', lambda event: render_chat(user, event))

    delete_button3 = Button(primus_canvas, 750, 40, './assets/delete_button3.png', None)
    delete_button3.bind('<Button-1>', lambda event: render_main_menu())

    gun_button3 = Button(primus_canvas, 820, 500, './assets/gun_button3.png', None)

    users_ids_list, users_names_list = private.list_user()

    i = 0
    for user_name in users_names_list:
        if user_name != user.get_name():      
            user_button = Button(primus_canvas, 20, 100 + 50 * i, './assets/gun_button_room.png', None)
            user_list_button.append(user_button)

            user_label = Label(primus_canvas, text=user_name, bg="black", font=("arial", 15), fg="white")
            user_label.place(x=60, y=110 + 50 * i )  
            user_label_list.append(user_label) 
            i += 1

    for button, id_user in zip(user_list_button, users_ids_list):
        button.bind('<Button-1>', lambda event, id=id_user: render_private_send(user, id, gun_button3, private, event))

    screen.mainloop()
    primus_canvas.update()

def render_private_send(user, id, gun_button3, private, event):
    global second_canvas, text_area

    if second_canvas is None:
        second_canvas = tk.Canvas(screen, width=630, height=350, bg="lightblue")
        second_canvas.pack(fill=tk.BOTH, expand=True)
        second_canvas.place(x=230, y=100)
    else :
        for widget in second_canvas.winfo_children():
            widget.destroy()  

    text_area = scrolledtext.ScrolledText(second_canvas, width=56, height=15, font=("Arial", 15), bg="black", fg="white", relief=tk.FLAT)
    
    gun_button3.bind('<Button-1>', lambda event=None, user=user, name_id=id: send_private_message(user, name_id, private, event))
    
    messages, name_ids = private.read_private_message()
    
    dates = []
    authors = []
    texts = []

    dates = [message[0] for message in messages]
    authors = [message[1] for message in messages]
    texts = [message[2] for message in messages]

    for messages, date, author, text, name_id in zip(messages, dates, authors, texts, name_ids):
        if name_id == id:
            text_area.insert(tk.INSERT, f"Date: {date}\nAuteur: {author}\nMessage: {text.replace('{', '').replace('}', '')}\n\n")

    text_area.configure(state ='disabled') 
    text_area.pack(fill=tk.BOTH, expand=True)

def send_private_message(user, name_id, private, event=None):
    global message_entry
    author = user.get_name()
    if message_entry :
        message_text_priv = message_entry[0][0].get_value()
        try:
            private.create_private_message(author, message_text_priv, name_id)
            message_entry[0][0].set_value("")
        except Exception as e:
            print(f"Error sending message: {e}")