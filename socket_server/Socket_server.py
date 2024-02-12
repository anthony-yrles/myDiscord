"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Class Socket_server facilite la création de server socket et est utilisé 
comme base pour créer des servers spécifique dans l'application
Enfant de la class Socket donc reçoit toutes les méthides dont send et receive
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from Socket import *

class Socket_server(Socket):
    """
    Méthode utilisé:

    accept_connection: Accept une connection entrante et renvoie un nouveau socket (client_socket)
    et l'adresse du client (client_adress)
    """

    def accept_connection(self):
        client_socket, client_address = self.accept()
        print(f"Connection from {client_address}")
        return client_socket, client_address
