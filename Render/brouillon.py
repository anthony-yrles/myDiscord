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


