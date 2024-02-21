import json
from User import User

class Authentication:
    def __init__(self, client):
        self.client = client
        
        self.user_list = []

    def get_client(self):
        return self.client
    def set_client(self, new_client):
        self.client = new_client

    def authenticate(self, mail, password):
        self.client.send_data('READ_TABLE_USER','')
        user_data_json = self.client.receive_data(1024)
        user_data_list = json.loads(user_data_json)
        if user_data_list:
            for user_data in user_data_list:
                name, surname, user_mail, user_password, list_room_private, list_room_group, list_created_room = user_data
                if user_mail == mail and user_password == password:
                    user = User(self.client, name, surname, user_mail, user_password, list_room_private, list_room_group, list_created_room)
                    if user not in self.user_list:
                        self.user_list.append(user)
                    return True, user
        return False
    
    def password_enter(password):
        autorized_Special_Char = "!@#$%^&*"
        if len(password) < 8 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char in autorized_Special_Char for char in password) or not any(char.isdigit() for char in password):
            return False
        return True
    
    def create_account(self, name, surname, mail, password):
        if self.password_enter(password):
            params = name, surname, mail, password
            self.client.send_data('CREATE_USER', params)
        
            # user_data_json = self.client.receive_data(1024)
            # user_data_list = json.loads(user_data_json)

        
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