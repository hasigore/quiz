import os
from gtts import gTTS
from playsound import playsound

class Audio:
    def __init__(self, audio_folder):
        self.audio_folder = audio_folder

    def generate_and_save_sound_if_missing(self, text, lang, sound_file):
        if not os.path.exists(sound_file):
            tts = gTTS(text=text, lang=lang)
            tts.save(sound_file)    
        
    def play(self, sound_file):
        playsound(sound_file)