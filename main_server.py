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

server_address = ('127.0.0.1', 1023)


host = "127.0.0.1"
user = "root"
password = "rootequipe7+"  
database = "mydiscord"

server = Server(server_address, host, user, password, database)
server.start()
server.start_listening()
