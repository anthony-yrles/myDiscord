"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Le fichier main_server.py est le point d'entrée du serveur. Il crée une
instance de Server et la démarre. Le serveur écoute ensuite les connexions
entrantes et gère les clients connectés.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from socket_server.Server import *
"""
server_address est un tuple contenant l'adresse IP du serveur et le port sur lequel le serveur doit écouter.
host, user, password et database sont les informations nécessaires pour se connecter à la base de données.
server est une instance de Server qui prend en paramètre server_address, host, user, password et database.
"""

host = "127.0.0.1"
user = "root"
password = "rootequipe7+"  
database = "mydiscord"

server = Server('127.0.0.1', 8080, 5, host, user, password, database)

running = True
try:
    while True:
        client_socket, client_address = server.accept_client()
        print(f"Accepted connection from {client_address}")
        
        data_received = client_socket.recv(1024)
        print(f"Received data: {data_received}")
        
        server.handle_client_request(client_socket)
        # server.send_data(client_socket, "Hello from server")

        user_input = input("Press 'q' to quit: ")
        if user_input.lower() == 'q':
            server.close()
            break
except Exception as e:
    print(f"Error: {e}")
finally:
    server.close()
    
