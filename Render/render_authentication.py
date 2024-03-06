import tkinter as tk
from tkinter import Label, scrolledtext, simpledialog
from Render.Render_image import Image
from Render.Render_Button import Button
from Render.Entry import CustomEntry
from Render.Writing_message import Writing_message
from Render.brouillon import list_room
from Authentication import Authentication
from socket_client.Client import Client
import threading


screen = tk.Tk()
screen.title("Talk to me!")
primus_canvas = tk.Canvas(screen, width=900, height=600)
primus_canvas.pack()

custom_entries = []
message_entry = []
area_message = []   
received_messages = []
displayed_messages = []
client = Client()
auth = Authentication(client)
second_canvas = None
text_area = None

run = False
update_event = threading.Event()
text_area_lock = threading.Lock()

def read_messages_loop(text_area):
    while run:
        data = client.receive_data(1024)
        if data :
            received_messages.append(data)
            refresh_messages(text_area)

    # Signaler au thread d'interface graphique de mettre à jour les messages
    update_event.set()



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
    return_authenticate = auth.authenticate(mail, password)
    if return_authenticate[0] == True:
        user = return_authenticate[1]
        
        client.connect_to_server('10.10.106.18', 8080)
        threading.Thread(target=read_messages_loop, args=(text_area)).start()
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
        
        # new_room_button = Button(primus_canvas, 20, 100 + 50 * len(room_button_list), './assets/gun_button.png', None)
        # new_room_button.bind('<Button-1>', render_message_send(user))
        # room_button_list.append(new_room_button)
        
        # new_room_label = Label(primus_canvas, text=room_name, bg="black", font=("arial", 15), fg="white")
        # new_room_label.place(x=60, y=110 + 27 * len(room_button_list))  
        # room_labels.append(new_room_label)

def render_create_message(user, event=None):
    enter_text = Writing_message(screen, "", x=260, y=491)    
    message_entry.append([enter_text])
    enter_text.set_value("")

def send_message(user, id_room, event=None):
    global received_messages
    author = user.get_name()
    message_text = message_entry[0][0].get_value()
    # print(message_text)
    try:
        user.create_message(author, message_text, id_room)
        message_entry[0][0].set_value("")
        # with text_area_lock:
        #     text_area.configure(state='normal')
        #     text_area.insert(tk.END, f"Message: {message_text}\n\n")
        #     text_area.configure(state='disabled')
    except Exception as e:
        print(f"Error sending message: {e}")
  

def render_chat(user, event=None):
    global room_button_list, room_labels
    run = True
    
    for entry in custom_entries:
        entry.destroy_entry()

    background_image = Image(primus_canvas, 0, 0, './assets/bcg_chat.png')
    background_image.draw()
 
    render_create_message(user)
 
    # enter_text = Writing_message(screen, "Write your message", x=260, y=491)    
    # custom_entries.append(enter_text)

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

    room_button_list, room_id_list = list_room(primus_canvas, user, room_button_list, room_labels, client.client_socket)

    for button, id_room in zip(room_button_list, room_id_list):
        button.bind('<Button-1>', lambda event, id=id_room: render_message_send(user, id, gun_button, event))


    screen.mainloop()
    primus_canvas.update()