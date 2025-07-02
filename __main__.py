from sources.config import Config
from sources.deck import Deck
from sources.quiz import Quiz
#from input import get_single_key

def main():
    config_file = 'decks/1/config.ini'
    config = Config(config_file=config_file)

    deck = Deck(config=config)

    quiz = Quiz(config=config, deck=deck)
    
    print(f"\nHeading: {deck.heading}")
    print(f"YouTube URL: {deck.url}\n")
    
    quiz.loop()
    quiz.loop_reverse()

if __name__ == "__main__":
    main()


