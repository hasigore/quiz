import os

from utils import normalize_text

def get_translations_from_file(translation_file, separator):
    with open(translation_file, 'r', encoding='utf-8') as f:
        heading = f.readline().strip()
        url = f.readline().strip()

        translations = []
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if separator in line:
                lang1, lang2 = line.split(separator, 1)
                translations.append((lang1.strip(), lang2.strip()))
            else:
                print(f"Warning: line does not contain '{separator}': {line}")

    return translations

def get_heading_from_file(translation_file):
    with open(translation_file, 'r', encoding='utf-8') as f:
        heading = f.readline().strip()
        url = f.readline().strip()

    return heading


def get_url_from_file(translation_file):
    with open(translation_file, 'r', encoding='utf-8') as f:
        heading = f.readline().strip()
        url = f.readline().strip()

    return url

def create_repeat_file_if_missing(repeat_file, translations, repeat, separator):
    if not os.path.exists(repeat_file):
        print(f"Initialize repeat file: {repeat_file}\n")
        with open(repeat_file, 'w', encoding='utf-8') as f:
            for source, target in translations:
                normalized_source = normalize_text(source)
                f.write(f"{normalized_source}{separator}{repeat}\n")

def refresh_repeats(repeat_file, separator):
    repeats = {}
    if not os.path.exists(repeat_file):
        return repeats
    
    with open(repeat_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(separator)
            if len(parts) == 2:
                source = parts[0].strip()
                repeat = int(parts[1].strip())
                repeats[source] = repeat
    return repeats

def save_repeats(repeat_filename, repeats, separator):
    with open(repeat_filename, 'w', encoding='utf-8') as f:
        for source, repeat in repeats.items():
            f.write(f"{source}{separator}{repeat}\n")

def decrement_phrase_repeat(phrase, repeats, repeat_file, separator):
    current_repeat = repeats[phrase]
    if current_repeat > 0:
        repeats[phrase] = current_repeat - 1
    else:
        repeats[phrase] = 0
    save_repeats(repeat_file, repeats, separator)
    return repeats 