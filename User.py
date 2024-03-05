from Room import Room
from datetime import datetime
from Text_room import Text_room
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

    def create_room(self, name, admin_name):
        params = (name, admin_name)
        self.client.send_data('CREATE_TEXT_ROOM', params)
        # self.add_room_to_list('text_room')

    def modify_room(self, name, list_modo, list_admin, list_user):
        self.name = name
        self.list_modo = list_modo
        self.list_admin = list_admin
        self.list_user = list_user


    def read_message(self):
        # print(f'1: {params}')
        self.client.send_data('READ_MESSAGE','')
        
        messages = self.client.receive_data(1073741824)
        # print(f'2: {messages}')
        messages = json.loads(messages)
        room_ids = [message[3] for message in messages]
        return messages, room_ids

    
    def show_room_data(self, type_of_room, client):
        params = (type_of_room,)
        self.client.send_data('SHOW_ROOM_DATA', params)
        user_data_json = self.client.receive_data(1024)
        
        try:
            user_data_list = json.loads(user_data_json)
        except json.JSONDecodeError:
            print("Error decoding JSON data")
            return False

        room_list = []

        if user_data_list:
            for user_data in user_data_list:
                id, name, list_admin, list_modo, list_user = user_data
                text_room = Text_room(name, list_admin, list_modo, list_user, client)
                room_list.append((id, text_room.get_name()))

            return room_list
        else:
            return False


    # def delete_room(self, name, list_room):
    #     for room in list_room:
    #         if room.name == name:
    #             list_room.remove(room)
    #             return f"Room '{name}' deleted successfully."
    #     return f"No room found with the name '{name}'."


    def create_message(self, author, message_text, id_room):
        hour = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # print(type(hour),"check le type mon pote")
        params = (hour, author, message_text, id_room)
        self.client.send_data('CREATE_NEW_MESSAGE', params)
    


    # def read_message(self, message_text):
    #     params = (message_text,)
    #     self.client.send_data('READ_TABLE_MESSAGE', params=None)
