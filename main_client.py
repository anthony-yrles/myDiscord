"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Le fichier main_client.py est le point d'entrée du client. Il crée une
instance de Client et se connecte au serveur. Le client envoie ensuite des
données au serveur et reçoit des réponses.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from socket_client.Client import *
from Authentication import *
from Text_room import *


"""
server_address est un tuple contenant l'adresse IP du serveur et le port sur lequel le serveur écoute.
client est une instance de Client qui prend en paramètre server_address.

"""

client = Client()

try:
    client.connect_to_server('127.0.0.1', 8080)

    running = True 
    while running:
        auth = Authentication(client)
        # auth.create_account('Serra', 'Mathis','mathis.serra@gmail.com', 'mdp1313mdp')
        list_message = Text_room('room_name', ['moderator1', 'moderator2'], ['admin1', 'admin2'], ['user1', 'user2'], client)
        list_message.read_all_mess()

        user_input = input("Press 'q' to quit: ")
        if user_input.lower() == 'q':
            client.close()
            break
except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()

