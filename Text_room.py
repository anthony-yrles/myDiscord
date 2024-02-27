import mysql.connector
from Room import Room
import json

class Text_room(Room):
    def __init__(self, name, list_modo, list_admin, list_user, client):
        super().__init__(name, list_modo, list_admin, list_user)
        self.client = client
        
    def read_all_mess(self):
        self.client.send_data('READ_TABLE_MESSAGE','')
        user_data_json = self.client.receive_data(1024)
        user_data_list = json.loads(user_data_json)
        for message in user_data_list:
            print(message)

    def notification(self):
        self.client.send_data('READ_LIST_ROOM_USER','')
        user_data_json = self.client.receive_data(1024)
        user_data_list = json.loads(user_data_json)
        for user in user_data_list:
            return user
        

    def create_message(self, hour, author, message_text, id_room):
        author = self.get_name()
        params = hour, author, message_text, id_room
        self.client.send_data('CREATE_MESSAGE', params)
        # user_data_json = self.client.receive_data(1024)
        # user_data_list = json.loads(user_data_json)
   

    def delete_message(self, id):
        params = id
        self.client.send_data('DELETE_MESSAGE', params)

