import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from User import User
from Render.render_authentication import client
import time

class Vocal_Recorder:
    def __init__(self, duration=3, samplerate=44100, channels=1):
        self.duration = duration
        self.samplerate = samplerate
        self.channels = channels
        
    def start_recording(self):
        print("Enregistrement en cours...")
        print('test')
        recorded_frames = sd.rec(int(self.duration * self.samplerate),
                                 samplerate=self.samplerate,
                                 channels=self.channels,
                                 dtype='int16')
        print('test1')
        sd.wait()
        print('test2')
        print("Enregistrement terminé.")
        
        return recorded_frames.astype(np.int16)

if __name__ == "__main__":
    # recorder = Vocal_Recorder()
    # recording = recorder.start_recording()
    # print(type(recording))
    # print(recording)
    # sd.play(recording, recorder.samplerate)
    # sd.wait()

    user = User(client, name='a', surname='a', mail='a', password='a')

    # write("recording0.wav", recorder.samplerate, recording)
    # recording_list = recording.tolist()
    # user.create_vocal_message("a", recording_list, 1)
    # print(type(recording))

    user.listen_message()
    message_list = user.listen_message()
    message_array = np.array(message_list, dtype=np.float32)
    sd.play(message_array, samplerate)
    sd.wait()
    time.sleep(2)

