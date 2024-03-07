from Socket import Socket

class Socket_client(Socket):
    """
    A client class for connecting to a server using sockets.

    """

    def __init__(self):
        super().__init__()

    def connect_to_server(self, address, port):
        """
        Connects to the server at the specified address and port.

        """
        self.connect(address, port)
        print(f"Connected to server at {address}:{port}")