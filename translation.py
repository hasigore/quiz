from file import get_translations_from_file, get_heading_from_file, get_url_from_file, create_repeat_file_if_missing, refresh_repeats, save_repeats

class Translation:
    def __init__(self, config):
        self._config = config 

    @property
    def language(self):
        return self._config.language
    
    @property
    def translation_file(self):
        return self._config.translation_file
    
    @property
    def separator(self):
        return self._config.separator
    
    @property
    def heading(self):
        if not hasattr(self, '_heading'):
            self._heading = get_heading_from_file(self.translation_file)
        return self._heading
    
    @property
    def url(self):
        if not hasattr(self, '_url'):
            self._url = get_url_from_file(self.translation_file)
        return self._url
    
    @property
    def translations(self):
        if not hasattr(self, '_translations'):
            self._translations = get_translations_from_file(self.translation_file, self.separator)
        return self._translations
    
    @property
    def repeat(self):
        return self._config.repeat
    
    @property
    def repeat_file(self):
        return self._config.repeat_file
    
    @property
    def reverse_repeat_file(self):
        return self._config.reverse_repeat_file
    
    @property
    def reverse_repeat(self):
        return self._config.reverse_repeat
    
    @property
    def repeats(self):
        create_repeat_file_if_missing(self.repeat_file, self.translations, self.repeat, self.separator)
        self._repeats = refresh_repeats(self.repeat_file, self.separator)
        return self._repeats
    
    @property
    def reverse_repeats(self):
        create_repeat_file_if_missing(self.reverse_repeat_file, self.translations, self.reverse_repeat, self.separator)
        self._reverse_repeats = refresh_repeats(self.reverse_repeat_file, self.separator)
        return self._reverse_repeats
    
    def __decrement_repeat(self, phrase, repeats, repeat_file, separator):
        if phrase in repeats:
            repeats[phrase] -= 1
            if repeats[phrase] < 0:
                repeats[phrase] = 0
            save_repeats(repeat_file, repeats, separator)
    
    def __increment_repeat(self, phrase, repeats, max_repeats, repeat_file, separator):
        if phrase in repeats:
            repeats[phrase] += 1
            if repeats[phrase] > max_repeats:
                repeats[phrase] = max_repeats
            save_repeats(repeat_file, repeats, separator)

    def increment_repeat(self, phrase):
        self._repeats = refresh_repeats(self.repeat_file, self.separator)
        self.__increment_repeat(phrase, self._repeats, self.repeat, self.repeat_file, self.separator)
    
    def increment_reverse_repeat(self, phrase):
        self._reverse_repeats = refresh_repeats(self.reverse_repeat_file, self.separator)
        self.__increment_repeat(phrase, self._reverse_repeats, self.reverse_repeat, self.reverse_repeat_file, self.separator)
    
    def decrement_repeat(self, phrase):
        self._repeats = refresh_repeats(self.repeat_file, self.separator)
        self.__decrement_repeat(phrase, self._repeats, self.repeat_file, self.separator)
        
    def decrement_reverse_repeat(self, phrase):
        self._reverse_repeats = refresh_repeats(self.reverse_repeat_file, self.separator)
        self.__decrement_repeat(phrase, self._reverse_repeats, self.reverse_repeat_file, self.separator)