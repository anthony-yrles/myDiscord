"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Le fichier main_client.py est le point d'entrée du client. Il crée une
instance de Client et se connecte au serveur. Le client envoie ensuite des
données au serveur et reçoit des réponses.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from socket_client.Client import *
from Authentication import *
from Render.current_render import state
import Render.current_render as Current_render

"""
server_address est un tuple contenant l'adresse IP du serveur et le port sur lequel le serveur écoute.
client est une instance de Client qui prend en paramètre server_address.

"""

client = Client()

try:
    client.connect_to_server('127.0.0.1', 8080)

    running = True 
    while running:

        state()()

        auth = Authentication(client)
        auth.create_account('Serra', 'Mathis','mathis.serra@gmail.com', 'mdp1313mdp')
        user = auth.authenticate("mathis.serra@gmail.com", "mdp1313mdp")
        user.show_user()

        user_input = input("Press 'q' to quit: ")
        if user_input.lower() == 'q':
            client.close()
            break
except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()

