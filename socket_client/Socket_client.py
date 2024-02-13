"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Class Socket_client facilite la création de client socket et est utilisé 
comme base pour créer des clients spécifique dans l'application
Enfant de la class Socket donc reçoit toutes les méthides dont send et receive
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from Socket import Socket

class Socket_client(Socket):
    """
    Méthode utilisé:

    connect_to_server: Permet la connection avec un serveur à une adresse spécifique.
    """

    def __init__(self):
        super().__init__()

    def connect_to_server(self, address, port):
        self.connect(address, port)
        print(f"Connected to server at {address}:{port}")