import os
from gtts import gTTS
# playsound3 is a fork of playsound that works with Python 3.10 and above, and is compatible with Windows, macOS, and Linux.
from playsound3 import playsound

class Audio:
    def __init__(self, audio_folder):
        self.audio_folder = audio_folder

    def generate_and_save_sound_if_missing(self, text, lang, sound_file):
        folder = os.path.dirname(sound_file)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
        if not os.path.exists(sound_file):
            tts = gTTS(text=text, lang=lang)
            tts.save(sound_file)    
        
    def play(self, sound_file):
        playsound(sound_file)