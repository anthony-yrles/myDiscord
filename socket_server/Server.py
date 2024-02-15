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
            'READ_TABLE_USER' : self.read_table_user
            }

    def accept_client(self):
        return self.server_socket.accept_connection()

    def close(self):
        self.server_socket.close()

    # def send_data(self, client_socket, data):
    #     if type(data) == list:
    #         for d in data:
    #             client_socket.send(d.encode())
    #     client_socket.send(data.encode())

    # def send_data(self, client_socket, data):
    #     if isinstance(data, list):
    #         for d in data:
    #             if isinstance(d, str):
    #                 client_socket.send(d.encode())
    #             elif isinstance(d, tuple):
    #                 for item in d:
    #                     if isinstance(item, str):
    #                         client_socket.send(item.encode())
    #                     elif isinstance(item, int) or isinstance(item, float):
    #                         client_socket.send(str(item).encode())
    #                     else:
    #                         print(f"Unsupported data type in tuple: {type(item)}")
    #             elif isinstance(d, int) or isinstance(d, float):
    #                 client_socket.send(str(d).encode())
    #             else:
    #                 print(f"Unsupported data type in list: {type(d)}")
    #     elif isinstance(data, str):
    #         client_socket.send(data.encode())
    #     else:
    #         print(f"Unsupported data type: {type(data)}")

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
    
    def handle_client_request(self, client_socket):
        client_data_received = client_socket.recv(1024).decode()
        if client_data_received in self.query_dictionnary:
            result = self.query_dictionnary[client_data_received]()
            self.send_data(client_socket, result)
        else:
            self.send_data("Command not recognized")

                
    #             break
    #         self.send_data_to_all_clients(data)

    # def start_listening(self):
    #     while True:
    #         client_socket, client_address = self.accept_connection()
    #         client = (client_socket, client_address)
    #         client_thread = threading.Thread(target=self.handle_client, args=(client,))
    #         client_thread.start()

    def create_user(self, username, password):
        query = "INSERT INTO user_table (username, password) VALUES (%s, %s)"
        params = (username, password)
        self.executeQuery(query, params)

    def check_username_availability(self, username):
        query = "SELECT * FROM user_table WHERE username = %s"
        params = (username,)
        result = self.fetch(query, params)
        return len(result) == 0

    def check_password_availability(self, password):
        query = "SELECT * FROM user_table WHERE password = %s"
        params = (password,)
        result = self.fetch(query, params)
        return len(result) == 0

    def authenticate_user(self, username, password):
        query = "SELECT * FROM user_table WHERE username = %s AND password = %s"
        params = (username, password)
        result = self.fetch(query, params)
        return len(result) > 0