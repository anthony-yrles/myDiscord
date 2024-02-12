"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Class Socket_client facilite la création de client socket et est utilisé 
comme base pour créer des clients spécifique dans l'application
Enfant de la class Socket donc reçoit toutes les méthides dont send et receive
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from Socket import Socket

class Socket_client(Socket):
    """
    Méthode utilisé:

    connect: Permet la connection avec un serveur à une adresse spécifique. 
    L'argument adresse est un tupple adresse IP du serveur + Port
    """

    def connect(self, address):
        self.socket.connect(address)
