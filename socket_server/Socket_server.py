from Socket import Socket

class Socket_server(Socket):

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
