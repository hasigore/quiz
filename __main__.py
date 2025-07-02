from config import Config
from translation import Translation
from quiz import Quiz
#from input import get_single_key

def main():
    config_file = 'config.ini'
    config = Config(config_file=config_file)

    translation = Translation(config=config)

    quiz = Quiz(config=config, translation=translation)
    
    print(f"\nHeading: {translation.heading}")
    print(f"YouTube URL: {translation.url}\n")
    
    quiz.loop()
    quiz.loop_reverse()

if __name__ == "__main__":
    main()


