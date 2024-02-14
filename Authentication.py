

class Authentication:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    
    def creation_account(self, client):
        client.send_data([])
        return "Account created"
    

    



