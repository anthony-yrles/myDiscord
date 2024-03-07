from socket_server.Socket_server import Socket_server
from socket_server.Singleton_Meta import SingletonMeta
from socket_server.Db import Db
import json
import threading
import http.server
import hashlib
from http.server import ThreadingHTTPServer
from .HttpServer import HttpServer

class Server(metaclass=SingletonMeta):

    client_connected = {}

    def __init__(self, address, port, backlog, host, user, password, database):
        self.db = Db(host, user, password, database)
        self.server_socket = Socket_server()
        self.server_socket.start(address, port, backlog)
        self.query_dictionnary = {
            'READ_TABLE_USER' : self.read_table_user,
            'READ_LIST_USER' : self.list_user,
            'CREATE_USER' : self.create_user,
            'READ_LIST_ROOM_USER' : self.read_list_room_user,
            'CREATE_NEW_MESSAGE' : self.create_new_message,
            'CREATE_NEW_VOCAL_MESSAGE': self.create_new_vocal_message,
            'CREATE_NEW_PRIVATE_MESSAGE' : self.create_new_private_message,
            'READ_MESSAGE' : self.read_message,
            'READ_PRIVATE_MESSAGE' : self.read_private_message,
            'LISTEN_VOCAL' : self.listen_vocal,
            'DELETE_MESSAGE' : self.delete_message,
            'MODIFY_MESSAGE' : self.modify_message,
            'MODIFY_REACTION_COUNT' : self.modify_reaction_count,
            'CREATE_TEXT_ROOM' : self.create_text_room,
            'CREATE_VOCAL_ROOM' : self.create_vocal_room,
            'SHOW_ROOM_DATA' : self.show_room_data
            }

    def run(server_class=ThreadingHTTPServer, handler_class=HttpServer, port=8888):
        server_address = ('127.0.0.1', port)
        httpd = server_class(server_address, handler_class)
        try:
            thread = threading.Thread(None, httpd.serve_forever, args=(threading.Event().set(),))
            thread.start()

        except KeyboardInterrupt:
            thread.join()
            httpd.shutdown()

    def accept_client(self):
        while True :
            print("Waiting for client connection...")
            client_socket, client_address = self.server_socket.accept_connection()
            self.client_connected[client_address] = client_socket
            print(f"Client {self.client_connected} connected")
            print("Starting client thread...")
            client_thread = threading.Thread(target=self.handle_client_request, args=(client_socket,))
            client_thread.start()
            print("Client thread started")

    def close(self):
        self.server_socket.close()

    def send_data(self, client_socket, data):
        try:
            json_data = json.dumps(data)
            client_socket.send(json_data.encode())
        except Exception as e:
            print(f"Error sending data: {e}")
    
    def read_table_user(self, mail):
        query = f'SELECT * FROM user WHERE mail = %s'
        params = (mail,)
        return self.db.fetch(query, params)
    
    def list_user(self):
        query = f'SELECT id, name FROM user'
        return self.db.fetch(query, params=None)
    
    def create_user(self, name, surname, mail, password, list_room_private = '{}', list_room_group = '{"Bienvenue"}', list_created_room = '{}'):
        password_bytes = password.encode('utf-8')
        hash_password = hashlib.sha256()
        hash_password.update(password_bytes)
        hashed_password = hash_password.hexdigest()
        query = f'INSERT INTO USER (name, surname, mail, password, list_room_private, list_room_group, list_created_room) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        params = (name, surname, mail, hashed_password, list_room_private, list_room_group, list_created_room)
        self.db.executeQuery(query, params)

    def create_text_room(self, name, list_admin, list_modo = '', list_user = ''):
        query = f'INSERT INTO text_room (name, list_admin, list_modo,  list_user) VALUES (%s, %s, %s, %s)'
        params = name, list_admin, list_modo, list_user
        self.db.executeQuery(query, params)

    def create_vocal_room(self, name, list_admin, list_modo = '', list_user = ''):
        query = f'INSERT INTO vocal_room (name, list_admin, list_modo,  list_user) VALUES (%s, %s, %s, %s)'
        params = name, list_admin, list_modo, list_user
        self.db.executeQuery(query, params)

    def read_list_room_user(self):
        query = f'SELECT list_user FROM text_room'
        return self.db.fetch(query, params=None)
    
    def send_to_all_clients(self, message):
        for client_socket in self.client_connected.values():
            self.send_data(client_socket, message)

    def create_new_message(self, hour, author, message_text, id_room):
        query = 'INSERT INTO message (hour, author, message_text, id_room) VALUES (%s, %s, %s, %s)'
        params = (hour, author, message_text, id_room)
        self.db.executeQuery(query, params)
        self.send_to_all_clients(params)

    def create_new_private_message(self, hour, author, message, id_user):
        query = 'INSERT INTO private_message (hour, author, message, id_user) VALUES (%s, %s, %s, %s)'
        params = (hour, author, message, id_user)
        self.db.executeQuery(query, params)
 

    def create_new_vocal_message(self, hour, author, message_vocal, id_room):
        query = 'INSERT INTO vocal_message (hour, author, message_vocal, id_room) VALUES (%s, %s, %s, %s)'
        params = (hour, author, message_vocal, id_room)
        try:
            self.db.executeQuery(query, params)
            print("Query executed")
        except Exception as e:
            print("Error executing query:", e)
            
    def read_message(self):
        query = f'SELECT hour, author, message_text, id_room FROM message'
        return self.db.fetch(query, params=None)
    
    def read_private_message(self):
        query = f'SELECT hour, author, message, id_user FROM private_message'
        return self.db.fetch(query, params=None)

    def listen_vocal(self):
        query = f'SELECT hour, author, message_vocal, id_room FROM vocal_message'
        return self.db.fetch(query, params=None)

    def delete_message(self, id):
        query = f'DELETE FROM message WHERE id = %s'
        params = (id,)
        self.db.executeQuery(query, params)

    def show_room_data(self, room_type):
        query = f'SELECT * FROM {room_type}'
        
        return self.db.fetch(query, params=None)

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
                client_data_received = client_socket.recv(1073741824).decode()
                print(client_data_received)
                if not client_data_received:
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
            client_socket.close()