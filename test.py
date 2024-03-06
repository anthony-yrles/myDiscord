# import numpy as np
# import soundfile as sf
# import json  # Import de la bibliothèque json pour la sérialisation
# from Vocal_message import Vocal_Recorder
# from User import User
# from Render.render_authentication import client

# user = User(client, name='a', surname='a', mail='a', password='a')

# # Enregistrement d'un message vocal avec Vocal_Recorder
# recorder = Vocal_Recorder(filename="temp_recording.wav")
# recorder.start_recording()
# recorder.save_recording()

# # Récupération des données audio sous forme de tableau matriciel
# audio_file_path = "temp_recording.wav"
# # Lecture du fichier audio et conversion en tableau matriciel
# with open(audio_file_path, 'rb') as file:
#     audio_data, _ = sf.read(file)
#     audio_list = audio_data.tolist()
# # Obtention de l'auteur du message (peut être remplacé par un nom d'utilisateur réel)
# author = "a"
# # Création du message vocal dans la base de données
# user.create_vocal_message(author, audio_list, id_room=1)

import soundfile as sf
from Vocal_message import Vocal_Recorder
from User import User
from Render.render_authentication import client

# Création d'une instance de l'utilisateur
user = User(client, name='a', surname='a', mail='a', password='a')

# Enregistrement d'un message vocal avec Vocal_Recorder
recorder = Vocal_Recorder()
recorded_data = recorder.start_recording()

# Enregistrement des données audio dans un fichier temporaire
temp_audio_file = "temp_recording.wav"
sf.write(temp_audio_file, recorded_data, recorder.samplerate)

# Lecture du fichier audio et conversion en tableau matriciel
with open(temp_audio_file, 'rb') as file:
    audio_data, samplerate = sf.read(file)
    audio_list = audio_data.tolist()

# Obtention de l'auteur du message (peut être remplacé par un nom d'utilisateur réel)
author = "a"

# Création du message vocal dans la base de données
user.create_vocal_message(author, audio_list, id_room=1)
print(type(audio_list))
user.listen_message()