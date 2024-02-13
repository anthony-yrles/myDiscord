"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Class Socket permettant de lier la partie serveur et la partie client
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import socket as sk

class Socket:

    """
    Méthode utilisé:

    bind: Lie le socket a l'attibut adresse, l'adresse doit être un tupple contenant IP et port

    listen: Ecoute les connections entrante et les mets en attente. 
    Backlog précise le nombre maximum de connexion en attente

    accept: Attend et accepte les connections entrantes. 
    Elle return la création d'une nouvelle socket avec le tupple adresse du client

    close: Ferme le socket et libere les ressources

    send: Envoie les données spécifiés (data) à la connexion (connection). 
    Les données sont encodés en bytes avant envoi

    receive: Recoit les données de connexion (connection). 

    Buffer_size est la taille des données maximum a recevoir simultanement. 
    Les données sont ensuite encodé en string et renvoyer
    """

    def __init__(self):
        self.socks= sk.socket(sk.AF_INET, sk.SOCK_STREAM)

    def bind(self, address):
        self.socks.bind(address)

    def listen(self, backlog):
        self.socks.listen(backlog)

    def accept(self):
        return self.socks.accept()

    def close(self):
        self.socks.close()

    def send(self, connection, data):
        connection.sendall(data.encode())

    def receive(self, connection, buffer_size=1024):
        return connection.recv(buffer_size).decode()