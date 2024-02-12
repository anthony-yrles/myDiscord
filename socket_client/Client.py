"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Class Client simplifie les interractions avec le serveur côté client.
Prend en argument un objet de Socket_client et en utilise les méthodes
ainsi que l'adresse du serveur
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from socket_client.Socket_client import Socket_client

class Client:

    """
    Méthode utilisé:
    connect: Connecte le Client au serveur via la class Socket_client

    send_data: Utilise la méthode send de Socket_client pour envoyer les demandes au serveur
    prend en argument les datas a envoyer

    receive_data: Utilise la méthode receive de Socket_client, l'argument buffer_size est la taille
    maximum des données recevable d'un seul coup

    close_connection: Utilise la méthode close de Socket_client pour fermer la connexion au serveur
    """
    def __init__(self, server_address):
        self.socket_client = Socket_client()
        self.server_address = server_address

    def connect(self):
        self.socket_client.connect(self.server_address)

    def send_data(self, data):
        self.socket_client.send(data)

    def receive_data(self, buffer_size=1024):
        return self.socket_client.receive(buffer_size)

    def close_connection(self):
        self.socket_client.close()
