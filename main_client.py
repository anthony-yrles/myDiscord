"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Le fichier main_client.py est le point d'entrée du client. Il crée une
instance de Client et se connecte au serveur. Le client envoie ensuite des
données au serveur et reçoit des réponses.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from socket_client.Client import *
from Authentication import *
from Text_room import *
from Render.current_render import state


"""
server_address est un tuple contenant l'adresse IP du serveur et le port sur lequel le serveur écoute.
client est une instance de Client qui prend en paramètre server_address.

"""

try:
    running = True 
    while running:

        state ()()


        user_input = input("Press 'q' to quit: ")
        if user_input.lower() == 'q':
            break
except Exception as e:
    print(f"Error: {e}")
# finally:
    # client.close()