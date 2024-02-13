"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Class Server simplifie les interractions avec le client côté server.
Prend en argument un objet de Socket_server et en utilise les méthodes
ainsi que l'adresse du server et une liste des clients
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import threading
from socket_server.Socket_server import Socket_server
from socket_server.Db import Db

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

    def accept_client(self):
        return self.server_socket.accept_connection()

    def close(self):
        self.server_socket.close()

    # def handle_client(self, client_socket):
    #     while True:
    #         data = self.receive_data(client_socket)
    #         if not data:
    #             self.close_connection(client_socket)
                
    #             break
    #         self.send_data_to_all_clients(data)

    # def start_listening(self):
    #     while True:
    #         client_socket, client_address = self.accept_connection()
    #         client = (client_socket, client_address)
    #         client_thread = threading.Thread(target=self.handle_client, args=(client,))
    #         client_thread.start()

