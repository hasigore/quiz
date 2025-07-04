import os

from sources.config import Config
from sources.deck import Deck
from sources.quiz import Quiz

def config_file_is_not_valid(config_file=None):
    if not config_file:
        print("No config file provided.")
        return True
    if not config_file.endswith('.ini'):
        print("Config file must be an .ini file.")
        return True
    config_directory = os.path.dirname(config_file)
    if not os.path.exists(config_directory):
        print(f"Config directory does not exist: {config_directory}")
        return True 
    if not os.path.isfile(config_file):
        print(f"Config file does not exist: {config_file}")
        return True
    return False

def main():
    config_file = 'decks/italienisch/italienisch–wortschatz-fuer-die-anfaenger-a1-a2/config.ini'
    if config_file_is_not_valid(config_file=config_file):
        print(f"Invalid config file: {config_file}")
        return
    
    config = Config(config_file=config_file)

    print(f"\nHeading: {config.deck_file}\n")
    deck = Deck(config=config)

    quiz = Quiz(config=config, deck=deck)
    
    print(f"\nHeading: {deck.heading}")
    print(f"URL: {deck.url}\n")
    
    quiz.loop()
    quiz.loop_reverse()

if __name__ == "__main__":
    main()


