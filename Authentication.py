import json
from User import User

class Authentication:
    def __init__(self, client):
        self.client = client
        self.user_list = []

    # def authenticate(self, mail, password):
    #     self.client.send_data('READ_TABLE_USER')
    #     user_data = self.client.receive_data(1024)
    #     if 'mail' in user_data and 'password' in user_data:
    #         if user_data['mail'] == mail and user_data['password'] == password:
    #             if user_data['name'] not in self.user_list:
    #                 user_data['name'] = User(user_data['name'], user_data['surname'], user_data['mail'], user_data['password'], user_data['list_room_private'], user_data['list_room_group'], user_data['list_created_room'])
    #                 self.user_list.append(user_data['name'])
    #                 return user_data['name']
    #     return False

    def authenticate(self, mail, password):
        self.client.send_data('READ_TABLE_USER')
        user_data_json = self.client.receive_data(1024)
        user_data_list = json.loads(user_data_json)
        if user_data_list:
            user_data = user_data_list[0]
            user_id, name, surname, user_mail, user_password, list_room_private, list_room_group, list_created_room = user_data
            if user_mail == mail and user_password == password:
                user = User(name, surname, user_mail, user_password, list_room_private, list_room_group, list_created_room)
                if user not in self.user_list:
                    self.user_list.append(user)
                return user
        return False
        
    # def login(self):
    #     if self.authenticate():
    #         return "Login successful"
    #     else:
    #         return "Login failed"
    
    # def logout(self):
    #     return "Logout successful"
    
    # def creation_account(self, client):
    #     client.send_data([])
    #     return "Account created"
    
    # def test_name(self):
    #     if self.username == "admin":
    #         return "Username already taken"
    #     else:
    #         return "Username available"
        
    # def test_password(self):
    #     if self.password == "admin":
    #         return "Password already taken"
    #     else:
    #         return "Password available"
        
    # def change_password(self, new_password):
    #     self.password = new_password
    #     return "Password changed"
    

# Test
# auth = Authentication("admin", "admin")