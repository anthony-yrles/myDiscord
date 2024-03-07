from Socket import Socket

class Socket_client(Socket):

    def __init__(self):
        super().__init__()

    def connect_to_server(self, address, port):
        self.connect(address, port)
        print(f"Connected to server at {address}:{port}")