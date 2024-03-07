from socket_client.Socket_client import Socket_client
import json

class Client:
    """
    Represents a client that connects to a server using a socket.

    """

    def __init__(self):
        self.client_socket = Socket_client()

    def connect_to_server(self, address, port):
        """
        Connects the client to the server at the specified address and port.

        """
        self.client_socket.connect_to_server(address, port)

    def send_data(self, method, params):
        """
        Sends data to the server using the client socket.

        """
        data = {'method': method, 'params': params}
        data_json = json.dumps(data)
        self.client_socket.send(data_json)
 
    def receive_data(self, buffer_size):
        """
        Receives data from the server using the client socket.

        """
        return self.client_socket.receive(buffer_size)

    def close(self):
        """
        Closes the client socket connection.

        """
        self.client_socket.close()