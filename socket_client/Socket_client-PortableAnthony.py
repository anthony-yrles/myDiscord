class SocketClient(Socket):
    def connect(self, address):
        self.socket.connect(address)

    def send(self, data):
        self.socket.sendall(data.encode())
