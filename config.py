import configparser
import os

class Config:
    def __init__(self, config_file='config.ini'):
        self.config_file = config_file
        self._config = configparser.ConfigParser()
        self._config.read(config_file, encoding='utf-8')
    
    def get(self, section, option, fallback=None):
        return self._config.get(section, option, fallback=fallback)

    def get_int(self, section, option, fallback=None):
        return self._config.getint(section, option, fallback=fallback)
    
    @property
    def translation_file(self):
        path = self.get('Settings', 'translation_file').strip("'\"")
        return os.path.abspath(path)
    
    @property
    def repeat(self):
        return self.get_int('Settings', 'repeat', fallback=3)

    @property
    def audio_folder(self):
        path = self.get('Settings', 'audio_folder').strip("'\"")
        return os.path.abspath(path)
    
    @property
    def repeat_file(self):
        repeat_file = self.translation_file.replace('.txt', '-repeat.txt')
        return repeat_file
    
    @property
    def reverse_repeat_file(self):
        reverse_repeat_file = self.translation_file.replace('.txt', '-reverse-repeat.txt')
        return reverse_repeat_file
    
    @property
    def separator(self):
        return self.get('Settings', 'separator', fallback=' : ').strip("'\"")
    
    @property
    def language(self):
        return self.get('Settings', 'language', fallback='it').strip("'\"")
    
    @property
    def audio_extension(self):
        return self.get('Settings', 'audio_extension', fallback='mp3').strip("'\"")
    
    @property
    def reverse_repeat(self):
        return self.get_int('Settings', 'reverse_repeat', fallback=3)