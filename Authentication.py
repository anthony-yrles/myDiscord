import requests
import hashlib
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
        data = {'method': ('READ_TABLE_USER'), 'params': (mail,)}
        try:
            user_data = requests.post('http://10.10.107.118:8888', json=data)
            user_data.raise_for_status()
            response_data = user_data.json()
            password = hashlib.sha256(password.encode()).hexdigest()
            print(password)

            if mail == response_data[0][3] and password == response_data[0][4]:
                user = User(self.client, response_data[0][1], response_data[0][2], response_data[0][3], response_data[0][4], response_data[0][5], response_data[0][6], response_data[0][7])
                return True, user

        except requests.exceptions.HTTPError as http_err:
            print(f'Erreur HTTP: {http_err}')

        except requests.exceptions.JSONDecodeError as json_err:
            print(f'Erreur de décodage JSON: {json_err}')

        except Exception as err:
            print(f'Erreur inattendue: {err}')

        return False, None
    
    def password_enter(password):
        autorized_Special_Char = "!@#$%^&*"
        if len(password) < 8 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char in autorized_Special_Char for char in password) or not any(char.isdigit() for char in password):
            return False
        return True
    
    def create_account(self, name, surname, mail, password):
        data = {'method': ('CREATE_USER'), 'params': (name, surname, mail, password)}
        user_data = requests.post('http://10.10.107.118:8888', json=data)
        user_data.raise_for_status()