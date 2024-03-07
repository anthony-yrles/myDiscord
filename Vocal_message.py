import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
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
                                 dtype='float32')

        sd.wait()
        recording_list = recorded_frames.tolist()
        user.create_vocal_message("a", recording_list, 1)
        # return recorded_frames.astype(np.int16)


    
