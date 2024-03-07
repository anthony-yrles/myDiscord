import socket as sk

class Socket:

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
        data = b""
        while True:
            chunk = self.socks.recv(buffer_size)
            if not chunk:
                break
            data += chunk
            if len(chunk) < buffer_size:
                break
        return data.decode()

    def close(self):
        self.socks.close()
