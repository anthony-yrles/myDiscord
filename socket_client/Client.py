from socket_client.Socket_client import Socket_client
import json

class Client:

    def __init__(self):
        self.client_socket = Socket_client()

    def connect_to_server(self, address, port):
        self.client_socket.connect_to_server(address, port)

    def send_data(self, method, params):
        data = {'method': method, 'params': params}
        data_json = json.dumps(data)
        self.client_socket.send(data_json)
 
    def receive_data(self, buffer_size):
        return self.client_socket.receive(buffer_size)

    def close(self):
        self.client_socket.close()