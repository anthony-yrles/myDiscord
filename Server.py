import socket
import threading
from Db import Db

host = "127.0.0.1"
port = 1023

class Server:
    def __init__(self):
        self.db = Db(host, "root", "rootequipe7+", "mydiscord")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(5)
        print(f"Server listening on {host}:{port}")

    def handle_client(self, socket_client):
        pass

    def start(self):
        while True:
            client, addr = self.sock.accept()
            print(f"Accepted connection from {addr[0]}:{addr[1]}")
            client_handler = threading.Thread(target=self.handle_client, args=(client,))
            client_handler.start()

# if __name__ == "__main__":
#     server = Server()
#     server.start()
