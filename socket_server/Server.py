"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Class Server simplifie les interractions avec le client côté server.
Prend en argument un objet de Socket_server et en utilise les méthodes
ainsi que l'adresse du server et une liste des clients
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from socket_server.Socket_server import Socket_server
from socket_server.Db import Db
import json
import threading

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
            'CREATE_NEW_MESSAGE' : self.create_new_message,
            'DELETE_MESSAGE' : self.delete_message,
            'MODIFY_MESSAGE' : self.modify_message,
            'MODIFY_REACTION_COUNT' : self.modify_reaction_count,
            'CREATE_TEXT_ROOM' : self.create_text_room,
            }

    def accept_client(self):
        while True:
            client_socket, client_address = self.server_socket.accept_connection()
            # Créer un thread pour gérer la requête du client
            client_thread = threading.Thread(target=self.handle_client_request, args=(client_socket,))
            # Démarrer le thread
            client_thread.start()

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
    
    def create_user(self, name, surname, mail, password, list_room_private = '{}', list_room_group = '{"Bienvenue"}', list_created_room = '{}'):
        query = f'INSERT INTO USER (name, surname, mail, password, list_room_private, list_room_group, list_created_room) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        params = (name, surname, mail, password, list_room_private, list_room_group, list_created_room)
        self.db.executeQuery(query, params)

    def create_text_room(self, name, list_admin, list_modo = '', list_user = ''):
        query = f'INSERT INTO text_room (name, list_admin, list_modo,  list_user) VALUES (%s, %s, %s, %s)'
        params = name, list_admin, list_modo, list_user
        self.db.executeQuery(query, params)

    def read_table_message(self):
        query = f'SELECT * FROM message'
        return self.db.fetch(query, params=None)

    def read_list_room_user(self):
        query = f'SELECT list_user FROM text_room'
        return self.db.fetch(query, params=None)

    def create_new_message(self, hour, author, message_text, id_room):
        query = 'INSERT INTO message (hour, author, message_text, id_room) VALUES (%s, %s, %s, %s)'
        params = (hour, author, message_text, id_room)
        self.db.executeQuery(query, params)

    def delete_message(self, id):
        query = f'DELETE FROM message WHERE id = %s'
        params = (id,)
        self.db.executeQuery(query, params)

    def modify_message(self, new_message, id):
        query = f'UPDATE message SET message_text = %s WHERE id = %s'
        params = (new_message, id)
        self.db.executeQuery(query, params)

    def modify_reaction_count(self, reaction_count_1, reaction_count_2, id):
        query = f'UPDATE message SET reaction_count_1 = %s, reaction_count_2 = %s WHERE id = %s'
        params = (reaction_count_1, reaction_count_2, id)
        self.db.executeQuery(query, params)

    def handle_client_request(self, client_socket):
        try:
            while True:
                client_data_received = client_socket.recv(1024).decode()
                print(client_data_received)
                if not client_data_received:
                    # Si la connexion est fermée côté client, sortir de la boucle
                    break

                request_data = json.loads(client_data_received)
                method_name = request_data['method']
                params = request_data['params']

                if method_name in self.query_dictionnary:
                    result = self.query_dictionnary[method_name](*params)
                    self.send_data(client_socket, result)
                else:
                    self.send_data(client_socket, "Command not recognized")
        except Exception as e:
            print(f"Error handling client request: {e}")
        finally:
            # Assurez-vous de fermer la connexion à la fin du traitement
            client_socket.close()