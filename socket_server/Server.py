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
    start: Configure le socket en utilisant la méthode bind de Socket_server issu de Socket qui prend en attribut l'adresse du server
    et la méthode listen qui attend les connections, l'attribut est le nombre de connection en attente maximum

    accept_connection: Utilise la méthode accept_connection de Socket_server.
    Les informations client_socket et client_adress sont ensuite ajouté à la liste clients

    send_data_to_all_clients: Utilise la méthode send de Socket_server pour envoyer les informations
    mise à jour à tous les clients

    receive_data: Utilise la méthode receive de Socket_server pour recevoir les datas de clients

    close_connection: Ferme la connection avec un client spécifique grace à la méthode close de Socket_server
    puis supprime les information de la liste client

    handle_client: Vérifie continuellement si un client_socket spécifique existe. Lorsque qu'une nouvelle data
    est reçu de la part de ce client utilise la méthode receive_data. Lorsque le client_socket ne répond plus
    utilise la méthode close_connection.
    Gère aussi l'envoi à tous les clients des datas mise à jour avec la méthode send_data_to_all_clients

    start_listening: Dans une boucle continue accepte les connexions avec la méthode accept_connection en renvoyant un nouveau socket_client
    puis crée un Thread ("isolation") à part qui va appeler la méthode handle_client et permettre la gestion d'un client spécifique
    Pendant ce temps la méthode start_listening peut continuer à gérer les nouveaux clients
    """

    def __init__(self, server_address, host, user, password, database):
        self.db = Db(host, user, password, database)
        self.socket_server = Socket_server()
        self.server_address = server_address
        self.clients = []

    def start(self):
        self.socket_server.bind(self.server_address)
        self.socket_server.listen(5)

    def accept_connection(self):
        client_socket, client_address = self.socket_server.accept_connection()
        self.clients.append((client_socket, client_address))
        return client_socket, client_address

    def send_data_to_all_clients(self, data):
        for client_socket, _ in self.clients:
            self.socket_server.send(client_socket, data)

    def receive_data(self, client_socket, buffer_size=1024):
        return self.socket_server.receive(client_socket, buffer_size)

    def close_connection(self, client_socket):
        client_socket.close()
        self.clients.remove((client_socket, _))

    def handle_client(self, client_socket):
        while True:
            data = self.receive_data(client_socket)
            if not data:
                self.close_connection(client_socket)
                break
            self.send_data_to_all_clients(data)

    def start_listening(self):
        while True:
            client_socket, client_address = self.accept_connection()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
            client_thread.start()
