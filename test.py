# import tempfile
# import os
# from datetime import datetime
# from Vocal_message import Vocal_Recorder
# from User import User
# from Render.render_authentication import client

# # Création d'une instance de la classe User
# user = User(client,name = 'a', surname ='a', mail='a', password='a')

# # Enregistrement d'un message vocal avec Vocal_Recorder
# recorder = Vocal_Recorder(filename="temp_recording.wav")
# recorder.start_recording()
# input("Appuyez sur Entrée pour arrêter l'enregistrement...")
# recorder.save_recording()

# # Récupération du chemin du fichier enregistré
# audio_file_path = "temp_recording.wav"

# # Obtention de l'auteur du message (peut être remplacé par un nom d'utilisateur réel)
# author = "Utilisateur Test"

# # Obtention de la date et de l'heure actuelles
# hour = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# # Création du message vocal dans la base de données
# user.create_vocal_message(author, audio_file_path, id_room=1)

import base64
import tempfile
import os
from datetime import datetime
from Vocal_message import Vocal_Recorder
from User import User
from Render.render_authentication import client

user = User(client,name = 'a', surname ='a', mail='a', password='a')

# Enregistrement d'un message vocal avec Vocal_Recorder
recorder = Vocal_Recorder(filename="temp_recording.wav")
recorder.start_recording()
input("Appuyez sur Entrée pour arrêter l'enregistrement...")
recorder.save_recording()

# Récupération du chemin du fichier enregistré
audio_file_path = "temp_recording.wav"

# Lecture du contenu du fichier audio et encodage en base64
with open(audio_file_path, 'rb') as file:
    vocal_message_bytes = file.read()
    vocal_message_base64 = base64.b64encode(vocal_message_bytes).decode('utf-8')

# Obtention de l'auteur du message (peut être remplacé par un nom d'utilisateur réel)
author = "a"

# Obtention de la date et de l'heure actuelles
hour = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Création du message vocal dans la base de données
user.create_vocal_message(author, vocal_message_base64, id_room=100)
