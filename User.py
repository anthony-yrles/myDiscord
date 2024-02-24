from Room import Room
import json

class User:
    def __init__(self, client,name, surname, mail, password, list_room_private = {}, list_room_group = {}, list_created_room = {}):
        self.client = client
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

    def read_id_room(self):
        self.client.send_data('READ_ID_ROOM','')
        id_room = self.client.receive_data(1024)
        print(id_room)
        return id_room
    
    def read_name_room(self, id_room):
        params = [id_room]
        self.client.send_data('READ_NAME_ROOM', params)
        name_room = self.client.receive_data(1024)
        return name_room
        
    def add_room_to_list(self, list_type):
        id_room = self.read_id_room()
        params = (id_room, list_type)
        self.client.send_data('ADD_ROOM_TO_LIST', params)
        list_type.append(id_room)

    def create_room(self, name, admin_name):
        params = (name, admin_name)
        self.client.send_data('CREATE_TEXT_ROOM', params)
        # self.add_room_to_list('text_room')

    def modify_room(self, name, list_modo, list_admin, list_user):
        self.name = name
        self.list_modo = list_modo
        self.list_admin = list_admin
        self.list_user = list_user

    # def delete_room(self, name, list_room):
    #     for room in list_room:
    #         if room.name == name:
    #             list_room.remove(room)
    #             return f"Room '{name}' deleted successfully."
    #     return f"No room found with the name '{name}'."

        # def read_message(self, message_text):
        #     params = (message_text,)
        #     self.client.send_data('READ_TABLE_MESSAGE', params=None)