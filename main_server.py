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
password = "SKenan30mg/"  
database = "mydiscord"

server = Server('10.10.89.102', 8080, 5, host, user, password, database)

try:
    while True:
        client_socket, client_address = server.accept_client()        
        server.handle_client_request(client_socket)

except Exception as e:
    print(f"Error: {e}")
finally:
    server.close()
    
