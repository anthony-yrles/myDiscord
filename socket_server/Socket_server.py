"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Class Socket_server facilite la création de server socket et est utilisé 
comme base pour créer des servers spécifique dans l'application
Enfant de la class Socket donc reçoit toutes les méthides dont send et receive
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from Socket import Socket

class Socket_server(Socket):
    """
    Méthode utilisé:

    start: Permet de lancer les méthodes bind et listen de Socket

    accept_connection: Accept une connection entrante et renvoie un nouveau socket (client_socket)
    et l'adresse du client (client_adress)
    """

    def __init__(self):
        super().__init__()

    def start(self, address, port, backlog):
        self.bind(address, port)
        self.listen(backlog)
        print(f"Server listening on {address}:{port}")

    def accept_connection(self):
        client_socket, client_address = self.accept()
        print(f"Accepted connection from {client_address}")
        return client_socket, client_address
