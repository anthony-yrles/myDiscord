"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Class Server simplifie les interractions avec le client côté server.
Prend en argument un objet de Socket_server et en utilise les méthodes
ainsi que l'adresse du server et une liste des clients
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from socket_server.Socket_server import Socket_server
from socket_server.Db import Db
import json

class Server:

    """
    Méthode utilisé:

    accept_client: Permet d'accepter les connections aux server

    close: Ferme le socket
    """

    def __init__(self, address, port, backlog, host, user, password, database):
        self.db = Db(host, user, password, database)
        self.server_socket = Socket_server()
        self.server_socket.start(address, port, backlog)
        self.query_dictionnary = {
            'READ_TABLE_USER' : self.read_table_user,
            'CREATE_USER' : self.create_user,
            'READ_TABLE_MESSAGE' : self.read_table_message,
            'READ_LIST_ROOM_USER' : self.read_list_room_user,
            'CREATE_MESSAGE' : self.create_message,
            'DELETE_MESSAGE' : self.delete_message
            }

    def accept_client(self):
        return self.server_socket.accept_connection()

    def close(self):
        self.server_socket.close()

    def send_data(self, client_socket, data):
        try:
            # Convertir les données en JSON
            json_data = json.dumps(data)
            # Envoyer les données encodées
            client_socket.send(json_data.encode())
        except Exception as e:
            print(f"Error sending data: {e}")

    def read_table_user(self):
        query = f'SELECT * FROM user'
        return self.db.fetch(query, params=None)
    
    def create_user(self, name, surname, mail, password):
        query = f'INSERT INTO user (name, surname, mail, password) VALUES (%s, %s, %s, %s)'
        params = (name, surname, mail, password)
        self.db.executeQuery(query, params)

    def read_table_message(self):
        query = f'SELECT * FROM message'
        return self.db.fetch(query, params=None)

    def read_list_room_user(self):
        query = f'SELECT list_user FROM text_room'
        return self.db.fetch(query, params=None)

    def create_message(self, hour, author, message_text, id_room):
        query = f'INSERT INTO message (hour, author, message_text, id_room) VALUES (%s, %s, %s, %s)'
        params = (hour, author, message_text)
        self.db.executeQuery(query, params)

    def delete_message(self, id):
        query = f'DELETE FROM message WHERE id = %s'
        params = (id,)
        self.db.executeQuery(query, params)
    
    def handle_client_request(self, client_socket):
        client_data_received = client_socket.recv(1024).decode()
        request_data = json.loads(client_data_received)
    
        method_name = request_data['method']
        params = request_data['params']
    
        if method_name in self.query_dictionnary:
            # Utiliser la méthode et les paramètres séparément
            result = self.query_dictionnary[method_name](*params)
            self.send_data(client_socket, result)
        else:
            self.send_data("Command not recognized")

    # def create_user(self, username, password):
    #     query = "INSERT INTO user_table (username, password) VALUES (%s, %s)"
    #     params = (username, password)
    #     self.executeQuery(query, params)

    # def check_username_availability(self, username):
    #     query = "SELECT * FROM user_table WHERE username = %s"
    #     params = (username,)
    #     result = self.fetch(query, params)
    #     return len(result) == 0

    # def check_password_availability(self, password):
    #     query = "SELECT * FROM user_table WHERE password = %s"
    #     params = (password,)
    #     result = self.fetch(query, params)
    #     return len(result) == 0

    # def authenticate_user(self, username, password):
    #     query = "SELECT * FROM user_table WHERE username = %s AND password = %s"
    #     params = (username, password)
    #     result = self.fetch(query, params)
    #     return len(result) > 0