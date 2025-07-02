import random
import time
from utils import clear_screen
from audio import Audio
from utils import create_file_path, create_file_path
from keyreader import KeyReader

class Quiz:
    def __init__(self, config, translation):
        self.config = config
        self.translation = translation
        self.key_reader = KeyReader()
    
    @property
    def audio(self):
        if not hasattr(self, '_audio'):
            self._audio = Audio(self.config.audio_folder)
        return self._audio
    
    def generate_and_save_sound_if_missing(self, text, lang, sound_file):
        self.audio.generate_and_save_sound_if_missing(text, lang, sound_file)
    
    def still_items_to_repeat(self):
        if self.number_of_items_to_repeat(self.translation.repeats) > 0:
            return True
    
    def still_items_to_reverse_repeat(self):
        if self.number_of_items_to_repeat(self.translation.reverse_repeats) > 0:
            return True
    
    def number_of_items_to_repeat(self, repeats):
        return sum(1 for value in repeats.values() if value > 0)

    def loop(self):
        # Assign a "repeat count" to each sentence; start with 3 repetitions each
        clear_screen()
        
        #print("Press '1/y/f' if you know the translation, '0/n/j' if not and for 'e' exit.\n")
        #for phrase, repeat_count in self.translation.repeats.items():
        #    print(f"Phrase: {phrase} - Repeat count: {repeat_count}")
        current_normalized_phrase = None
        last_n_phrases = []
        number_of_phrases_to_remember = 3  # Number of phrases to remember in the last_n_phrases list
        while self.still_items_to_repeat():

            new_current_normalized_phrase = random.choice(list(self.translation.repeats.keys()))
            
            #print(f"Current phrase: {current_normalized_phrase}")
            current_repeat_count = self.translation.repeats[new_current_normalized_phrase]
            #print(f"Current repeat count: {current_repeat_count}")
            if current_repeat_count <= 0:
                continue
            
            number_of_items_to_repeat = self.number_of_items_to_repeat(self.translation.repeats)
            if new_current_normalized_phrase in last_n_phrases and number_of_items_to_repeat > number_of_phrases_to_remember:
                print(f"Skipping phrase {new_current_normalized_phrase} as it is in the last {number_of_phrases_to_remember} phrases.")
                print(f"Last phrases: {last_n_phrases}")
                continue
            current_normalized_phrase = new_current_normalized_phrase
            last_n_phrases.append(current_normalized_phrase)
            if len(last_n_phrases) > number_of_phrases_to_remember:
                last_n_phrases.pop(0)

            current_index = list(self.translation.repeats.keys()).index(current_normalized_phrase)   
            source, target = self.translation.translations[current_index]

            print(f"{source}")
            sound_file = create_file_path(self.audio.audio_folder, current_normalized_phrase, self.config.audio_extension)
            self.audio.generate_and_save_sound_if_missing(text=source, lang=self.translation.language, sound_file=sound_file)
            self.audio.play(sound_file)
            
            user_input = self.key_reader.read()
            
            if user_input.lower() == 'e':
                print("Exiting quiz.")
                break
            clear_screen()
            
            print(f"{source}")
            self.audio.play(sound_file)
            print(f"{target}\n\n")

            if user_input == '1':
                self.translation.decrement_repeat(phrase=current_normalized_phrase)
            
            if user_input == '0':
                self.translation.increment_repeat(phrase=current_normalized_phrase)

        print("Quiz complete! Well done.")
    
    


    def loop_reverse(self):
        # Assign a "repeat count" to each sentence; start with 3 repetitions each
        clear_screen()
        
        #print("Press '1/y/f' if you know the translation, '0/n/j' if not and for 'e' exit.\n")
        #for phrase, repeat_count in self.translation.reverse_repeats.items():
        #    print(f"Phrase: {phrase} - Repeat count: {repeat_count}")
        
        current_normalized_phrase = None
        last_n_phrases = []
        number_of_phrases_to_remember = 3  # Number of phrases to remember in the last_n_phrases list
        while self.still_items_to_reverse_repeat():

            new_current_normalized_phrase = random.choice(list(self.translation.reverse_repeats.keys()))

            #print(f"Current phrase: {current_normalized_phrase}")
            current_repeat_count = self.translation.reverse_repeats[new_current_normalized_phrase]
            #print(f"Current repeat count: {current_repeat_count}")

            if current_repeat_count <= 0:
                continue

            number_of_items_to_repeat = self.number_of_items_to_repeat(self.translation.reverse_repeats)
            #print(f"number_of_items_to_repeat: {number_of_items_to_repeat}")
            #print(f"Last {number_of_phrases_to_remember} phrases : {last_n_phrases}.")
            if new_current_normalized_phrase in last_n_phrases and number_of_items_to_repeat > number_of_phrases_to_remember:
                #print(f"Skipping phrase {new_current_normalized_phrase} as it is in the last {number_of_phrases_to_remember} phrases.")
                #print(f"Last phrases: {last_n_phrases}")
                continue

            current_normalized_phrase = new_current_normalized_phrase
            last_n_phrases.append(current_normalized_phrase)
            if len(last_n_phrases) > number_of_phrases_to_remember:
                last_n_phrases.pop(0)

            current_index = list(self.translation.reverse_repeats.keys()).index(current_normalized_phrase)   
            source, target = self.translation.translations[current_index]

            print(f"{target}")
            
            user_input = self.key_reader.read()
            
            if user_input.lower() == 'e':
                print("Exiting quiz.")
                break
            clear_screen()

            print(f"{target}")
            print(f"{source}\n\n")

            sound_file = create_file_path(self.audio.audio_folder, current_normalized_phrase, self.config.audio_extension)
            self.audio.generate_and_save_sound_if_missing(text=source, lang=self.translation.language, sound_file=sound_file)
            self.audio.play(sound_file)
            
            #if current_repeat_count == self.translation.reverse_repeat:
            #    time.sleep(3)  # Wait for 3 seconds before playing the sound again
            #    self.audio.play(sound_file)

            if user_input == '1':
                self.translation.decrement_reverse_repeat(phrase=current_normalized_phrase)
            
            if user_input == '0':
                self.translation.increment_reverse_repeat(phrase=current_normalized_phrase)

        print("Quiz complete! Well done.")
