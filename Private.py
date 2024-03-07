import json

class Private():
    def __init__(self, client):
        self.client = client
    
    def list_user(self):
        self.client.send_data('READ_LIST_USER', '')
        list_users = self.client.receive_data(1073741824)
        print(list_users)
        list_users = json.loads(list_users)
        users_ids = [list_user[0] for list_user in list_users]
        users_names = [list_user[1] for list_user in list_users]
        return users_ids, users_names
    
    def read_private_message(self):
        self.client.send_data('READ_PRIVATE_MESSAGE','')
        messages = self.client.receive_data(1073741824)
        messages = json.loads(messages)
        name_ids = [message[3] for message in messages]
        return messages, name_ids