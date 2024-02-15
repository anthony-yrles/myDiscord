"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Class Client simplifie les interractions avec le serveur côté client.
Prend en argument un objet de Socket_client et en utilise les méthodes
ainsi que l'adresse du serveur
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from socket_client.Socket_client import Socket_client
import json

class Client:
    """
    Méthodes utilisé:

    connect_to_server: Permet de conencter le client au server

    send_data: Permet d'envoyer des informations au server

    receive_data: Permet de recevoir des informations

    close: Ferme la connection au server
    """

    def __init__(self):
        self.client_socket = Socket_client()

    def connect_to_server(self, address, port):
        self.client_socket.connect_to_server(address, port)

    def send_data(self, method, params):
        data = {'method': method, 'params': params}
        data_json = json.dumps(data)
        self.client_socket.send(data_json)

    def receive_data(self, buffer_size):
        return self.client_socket.receive(buffer_size)

    def close(self):
        self.client_socket.close()