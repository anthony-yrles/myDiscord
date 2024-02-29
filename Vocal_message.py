import sounddevice as sd
import numpy as np
import wave

# class Vocal_Recorder:
#     def __init__(self, filename="recording.wav"):
#         self.filename = filename
#         self.samplerate = 44100
#         self.channels = 1
#         self.duration = 5 
        
#     def start_recording(self):
#         print("Enregistrement en cours...")
#         self.recorded_frames = sd.rec(int(self.duration * self.samplerate),
#                                       samplerate=self.samplerate,
#                                       channels=self.channels,
#                                       dtype='int16')
#         sd.wait()
#         print("Enregistrement terminé.")
        
#         self.save_recording()
    
#     def save_recording(self):
#         wf = wave.open(self.filename, 'wb')
#         wf.setnchannels(self.channels)
#         wf.setsampwidth(2)  
#         wf.setframerate(self.samplerate)
#         wf.writeframes(self.recorded_frames.tobytes())
#         wf.close()
        
#         print("Enregistrement sauvegardé sous", self.filename)
        
#     def play_recording(self):
#         mixer.init()
#         mixer.music.load(self.filename)
#         mixer.music.play()
#         while mixer.music.get_busy():
#             pygame.time.Clock().tick(10)
#         mixer.quit()

# # using example :
# if __name__ == "__main__":
#     recorder = Vocal_Recorder()
#     recorder.start_recording()
#     recorder.play_recording()

class Vocal_Recorder:
    def __init__(self, filename="recording.wav"):
        self.filename = filename
        self.samplerate = 44100
        self.channels = 1
        self.duration = 5 
        
    def start_recording(self):
        print("Enregistrement en cours...")
        self.recorded_frames = sd.rec(int(self.duration * self.samplerate),
                                      samplerate=self.samplerate,
                                      channels=self.channels,
                                      dtype='int16')
        sd.wait()
        print("Enregistrement terminé.")
        
        self.save_recording()
    
    def save_recording(self):
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(2)  
        wf.setframerate(self.samplerate)
        wf.writeframes(self.recorded_frames.tobytes())
        wf.close()
        
        print("Enregistrement sauvegardé sous", self.filename)
        
    def play_recording(self):
        print("Lecture de l'enregistrement...")
        data, fs = wave.read(self.filename)
        sd.play(data, fs)
        sd.wait()
        print("Lecture terminée.")

# using example :
if __name__ == "__main__":
    recorder = Vocal_Recorder()
    recorder.start_recording()
    recorder.play_recording()
