"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Class Client simplifie les interractions avec le serveur côté client.
Prend en argument un objet de Socket_client et en utilise les méthodes
ainsi que l'adresse du serveur
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from socket_client.Socket_client import Socket_client

class Client:
    """
    Classe Client qui simplifie les interactions avec le serveur côté client.
    Prend en argument un objet de Socket_client et en utilise les méthodes ainsi que l'adresse du serveur.
    """

    def __init__(self, server_address):
        self.socket_client = Socket_client()
        self.server_address = server_address

    def connect(self):
        self.socket_client.connect(self.server_address)

    def send_data(self, data):
        data_bytes = data.encode()
        self.socket_client.send(data_bytes)

    def receive_data(self, buffer_size=1024):
        return self.socket_client.receive(buffer_size)

    def close_connection(self):
        self.socket_client.close()