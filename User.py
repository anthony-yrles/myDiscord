from Room import Room
from datetime import datetime
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

    def create_message(self, author, message_text, id_room):
        hour = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        params = (hour, author, message_text, id_room)
        self.client.send_data('CREATE_NEW_MESSAGE', params)

    # def read_message(self, message_text):
    #     params = (message_text,)
    #     self.client.send_data('READ_TABLE_MESSAGE', params=None)
