import json

class Authentication:
    def __init__(self, client):
        self.client = client
        self.user_list = []

    def authenticate(self, email, password):
        self.client.send_data('READ_TABLE_USER')
        user_data_json = self.client.receive_data(1024)
        user_data = json.loads(user_data_json)
        if 'email' in user_data and 'password' in user_data:
            if user_data['email'] == email and user_data['password'] == password:
                if user_data['name'] not in self.user_list:
                    user_data['name'] = User(user_data['name'], user_data['prenom'], user_data['email'], user_data['password'], user_data['list_room_private'], user_data['list_room_group'], user_data['list_room_create'])
                    self.user_list.append(user_data['name'])
                    return user_data['name']
        return False
        
    def login(self):
        if self.authenticate():
            return "Login successful"
        else:
            return "Login failed"
    
    def logout(self):
        return "Logout successful"
    
    def creation_account(self):
        return "Account created"
    
    def test_name(self):
        if self.username == "admin":
            return "Username already taken"
        else:
            return "Username available"
        
    def test_password(self):
        if self.password == "admin":
            return "Password already taken"
        else:
            return "Password available"
        
    def change_password(self, new_password):
        self.password = new_password
        return "Password changed"
    

# Test
auth = Authentication("admin", "admin")