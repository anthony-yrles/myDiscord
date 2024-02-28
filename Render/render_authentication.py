import tkinter as tk
from tkinter import Label, scrolledtext, simpledialog
from Render.Render_image import Image
from Render.Render_Button import Button
from Render.Entry import CustomEntry
from Render.Writing_message import Writing_message
from Render.brouillon import list_room
from Authentication import Authentication
from socket_client.Client import Client
import time


screen = tk.Tk()
screen.title("Talk to me!")
primus_canvas = tk.Canvas(screen, width=900, height=600)
primus_canvas.pack()


custom_entries = []
message_entry = []
client = Client()
client.connect_to_server('10.10.96.156', 8080)
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


def render_message_send(user, id_room, gun_button, event=None):
    second_canvas = tk.Canvas(screen, width=630, height=350, bg="lightblue")
    second_canvas.pack(fill=tk.BOTH, expand=True)
    second_canvas.place(x=230, y=100)

    gun_button.bind('<Button-1>', lambda event: send_message(user, id_room, event))
    text_area = scrolledtext.ScrolledText(second_canvas, width=56, height=15, font=("Arial", 15), bg="black", fg="white") 
    messages, room_ids = user.read_message()
    
    dates = []
    authors = []
    texts = []

    dates = [message[0] for message in messages]
    authors = [message[1] for message in messages]
    texts = [message[2] for message in messages]

    print("DEBUG: All Messages:", messages)
    print("DEBUG: Type of All Messages:", type(messages))
    filtered_messages = [message[2] for message, room_id in zip(messages, room_ids) if room_id == id_room and isinstance(message, list)]


    print("DEBUG: Filtered Messages:", filtered_messages)
    for message, date, author, text in zip(messages, dates, authors, texts):
        if message[3] == id_room:  # Vérifie si l'ID de la salle correspond à celui spécifié
            text_area.insert(tk.INSERT, f"Date: {date}\nAuteur: {author}\nMessage: {text.replace('{', '').replace('}', '')}\n\n")



    text_area.configure(state ='disabled') 
    text_area.pack(fill=tk.BOTH, expand=True)

# def render_message_send(user, id_room, gun_button, event=None):
#     second_canvas = tk.Canvas(screen, width=630, height=350, bg="lightblue")
#     second_canvas.pack(fill=tk.BOTH, expand=True)
#     second_canvas.place(x=230, y=100)
    
#     gun_button.bind('<Button-1>', lambda event: send_message(user, event))

#     messages, room_ids = user.read_message()
#     print("niquez vous", messages)
#     dates = []
#     authors = []
#     texts = []

#     dates = [message[0] for message in messages]
#     authors = [message[1] for message in messages]
#     texts = [message[2] for message in messages]

#     filtered_messages = [message for message, room_id in zip(messages, room_ids) if room_id == id_room]
#     text_area = scrolledtext.ScrolledText(second_canvas, width=56, height=15, font=("Arial", 15), bg="black", fg="white") 
    
#     for message in messages:
#         if len(message) == 3:  
#             date, author, message_text = message
#             dates.append(date)
#             authors.append(author)
#             texts.append(message_text)
#         else:
#             print("Error: Message format incorrect:", message)

    # print("DEBUG: Dates:", dates)
    # print("DEBUG: Authors:", authors)
    # print("DEBUG: Texts:", texts)


    # print("DEBUG: All Messages:", all_messages)
    # print("DEBUG: Type of All Messages:", type(all_messages))
    # text_area.configure(state ='disabled') 

    # new_message = "A new message!"
    # text_area.configure(state='normal')
    # text_area.insert(tk.END, "\n" + new_message)
    # text_area.configure(state='disabled')




def render_create_room(user, event=None):
    global room_button_list, room_labels
    room_name = simpledialog.askstring("Nouvelle Room", "Entrez le nom de la nouvelle room:")  
    if room_name:
        user.create_room(room_name, user.get_name())
        
        new_room_button = Button(primus_canvas, 20, 100 + 50 * len(room_button_list), './assets/gun_button.png', None)
        new_room_button.bind('<Button-1>', render_message_send(user))
        room_button_list.append(new_room_button)
        
        new_room_label = Label(primus_canvas, text=room_name, bg="black", font=("arial", 15), fg="white")
        new_room_label.place(x=60, y=110 + 27 * len(room_button_list))  
        room_labels.append(new_room_label)

def render_create_message(user, event=None):
    enter_text = Writing_message(screen, "", x=260, y=491)    
    message_entry.append([enter_text])
    enter_text.set_value("")

def send_message(user, id_room, event=None):
    author = user.get_name()
    message_text = message_entry[0][0].get_value()
    print(message_text)
    try:
        user.create_message(author, message_text, id_room)
        print("Test3")
        message_entry[0][0].set_value("")
    except Exception as e:
        print(f"Error sending message: {e}")
   

def render_chat(user, event=None):
    global room_button_list, room_labels
    
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
    # gun_button.bind('<Button-1>', lambda event: send_message(user, id_room, event))

    room_button_list, room_id_list = list_room(primus_canvas, user, room_button_list, room_labels, client.client_socket)

    for button, id_room in zip(room_button_list, room_id_list):
        button.bind('<Button-1>', lambda event, id=id_room: render_message_send(user, id, gun_button, event))

    screen.mainloop()
    primus_canvas.update()