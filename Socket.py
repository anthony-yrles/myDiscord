"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Class Socket permettant de lier la partie serveur et la partie client
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import socket as sk

class Socket:

    """
    Méthode utilisé:

    bind: Lie le socket a l'attibut adresse, l'adresse doit être un tuple contenant IP et port

    listen: Ecoute les connections entrante et les mets en attente. 
    Backlog précise le nombre maximum de connexion en attente

    accept: Attend et accepte les connections entrantes. 
    Elle return la création d'une nouvelle socket avec le tupple adresse du client


    send: Envoie les données spécifiés (data). 
    Les données sont encodés en bytes avant envoi

    receive: Recoit les données. Buffer_size est la taille des données maximum a recevoir simultanement. 
    Les données sont ensuite encodé en string et renvoyer
    
    close: Ferme le socket et libere les ressources
    """

    def __init__(self):
        self.socks = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

    def bind(self, address, port):
        self.socks.bind((address, port))

    def listen(self, backlog):
        self.socks.listen(backlog)

    def accept(self):
        return self.socks.accept()

    def connect(self, address, port):
        self.socks.connect((address, port))

    def send(self, data):
        self.socks.send(data.encode())

    def receive(self, buffer_size):
        return self.socks.recv(buffer_size).decode()

    def close(self):
        self.socks.close()
