"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Le fichier main_client.py est le point d'entrée du client. Il crée une
instance de Client et se connecte au serveur. Le client envoie ensuite des
données au serveur et reçoit des réponses.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from socket_client.Client import *

"""
server_address est un tuple contenant l'adresse IP du serveur et le port sur lequel le serveur écoute.
client est une instance de Client qui prend en paramètre server_address.

"""

client = Client()
client.connect_to_server('10.10.74.165', 8080)
client.send_data("Hello, Wawa!")
client.close()