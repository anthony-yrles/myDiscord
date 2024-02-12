class Client:
    def __init__(self, server_address):
        self.socket_client = SocketClient()
        self.server_address = server_address

    def connect(self):
        self.socket_client.connect(self.server_address)

    def send_data(self, data):
        self.socket_client.send(data)

    def close_connection(self):
        self.socket_client.close()
