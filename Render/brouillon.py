from Render.Render_image import Image
from Render.Render_Button import Button
from tkinter import Label

def list_room(primus_canvas, user, room_button_list, room_labels, type_room, client):
    room_datas = user.show_room_data(type_room, client)
    room_id_list = []
    room_name_list = []

    for room_data in room_datas:
        room_id_list.append(room_data[0])
        room_name_list.append(room_data[1])

    i = 0
    for room_name in room_name_list:

        room_button = Button(primus_canvas, 20, 100 + 50 * i, './assets/gun_button.png', None)
        room_button_list.append(room_button)       
        room_button = Button(primus_canvas, 20, 100 + 50 * i, './assets/gun_button_room.png', None)
        # room_button.bind('<Button-1>', None)
        room_button_list.append(room_button)

        room_label = Label(primus_canvas, text=room_name, bg="black", font=("arial", 15), fg="white")
        room_label.place(x=60, y=110 + 50 * i )  
        room_labels.append(room_label) 
        i += 1

    return room_button_list, room_id_list


