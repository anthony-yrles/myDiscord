class User:
    def __init__(self, name, surname, mail, password, list_room_private = {}, list_room_group = {}, list_created_room = {}):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.password = password
        self.list_room_private = list_room_private
        self.list_room_group = list_room_group
        self.list_created_room = list_created_room

    #getter and setter for name
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    #getter and setter for surname
    def get_surname(self):
        return self.surname
    def set_surname(self, surname):
        self.surname = surname

    #getter and setter for mail
    def get_mail(self):
        return self.mail
    def set_mail(self, mail):
        self.mail = mail

    #getter and setter for password
    def get_password(self):
        return self.password
    def set_password(self, password):
        self.password = password

    #getter and setter for list_room_private
    def get_list_room_private(self):
        return self.list_room_private
    def set_list_room_private(self, list_room_private):
        self.list_room_private = list_room_private

    #getter and setter for list_room_group
    def get_list_room_group(self):
        return self.list_room_group
    def set_list_room_group(self, list_room_group):
        self.list_room_group = list_room_group

    #getter and setter for list_created_room
    def get_list_created_room(self):
        return self.list_created_room
    def set_list_created_room(self, list_created_room):
        self.list_created_room = list_created_room
    
    def show_list_room(self):
        list_room = {
            "list_room_private": self.list_room_private,
            "list_room_group": self.list_room_group
        }

        for type_room, list_room in list_room.items():
            print(f"{type_room}: {list_room}")
            if list_room:
                for room in list_room:
                    print(f"Room: {room}")
            else:
                print("No room")


    def show_list_created_room(self):
        print(f"list_created_room: {self.list_created_room}")
        for created_room in self.list_created_room:
            print(f"created room: {created_room}")

    def quit_room(self, room):
        if room in self.list_room_private:
            self.list_room_private.remove(room)
        elif room in self.list_room_group:
            self.list_room_group.remove(room)
        elif room in self.list_created_room:
            self.list_created_room.remove(room)
        else:
            print("Room not found")

    def show_user(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Mail: {self.mail}")
        print(f"Password: {self.password}")
        self.show_list_room()
        self.show_list_created_room()
        print("")

    #create a new room
    def create_room(self, name, list_modo, list_admin, list_user):
        return Room(name, list_modo, list_admin, list_user)

    #modify the room
    def modify_room(self, name, list_modo, list_admin, list_user):
        self.name = name
        self.list_modo = list_modo
        self.list_admin = list_admin
        self.list_user = list_user

    def delete_room(self, name, list_room):
        for room in list_room:
            if room.name == name:
                list_room.remove(room)
                return f"Room '{name}' deleted successfully."
        return f"No room found with the name '{name}'."