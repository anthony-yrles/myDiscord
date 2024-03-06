import sounddevice as sd
import numpy as np
# from scipy.io.wavfile import write
import time

class Vocal_Recorder:
    def __init__(self, duration=3, samplerate=44100, channels=1):
        self.duration = duration
        self.samplerate = samplerate
        self.channels = channels
        
    def start_recording(self, user):
        print("Recording...")
        recorded_frames = sd.rec(int(self.duration * self.samplerate),
                                 samplerate=self.samplerate,
                                 channels=self.channels,
                                 dtype='int16')

        sd.wait()
        recording_list = recorded_frames.astype(np.int16).tolist()
        user.create_vocal_message("a", recording_list, 1)
        # return recorded_frames.astype(np.int16)

if __name__ == "__main__":
    """
    partie création de message vocal et écoute sans enregistrement dans la db à décommenter pour tester
    """
    # recorder = Vocal_Recorder()
    # recording = recorder.start_recording()
    # sd.play(recording, recorder.samplerate)
    # sd.wait()

    """
    fin partie création de message vocal et écoute sans enregistrement dans la db
    """

    """
    partie création de message vocal et écoute avec enregistrement dans la db à décommenter (avec la première partie) pour tester 
    """

    """
    fin partie création de message vocal et écoute avec enregistrement dans la db
    """

    """
    partie écoute de message vocal (à décommenter pour tester) et commenter les autres parties
    """

    # user.listen_message()
    # message_list = user.listen_message()
    # message_array = np.array(message_list, dtype=np.float32)
    # sd.play(message_array, samplerate)
    # sd.wait()
    # time.sleep(2)
    """
    fin partie écoute de message vocal
    """

    
