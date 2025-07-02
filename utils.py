import os
import re

from unidecode import unidecode

def normalize_text(text):
    ascii_text = unidecode(text)
    ascii_text = ascii_text.lower()
    ascii_text = re.sub(r"[’'`]", "_", ascii_text)
    ascii_text = ascii_text.replace(' ', '_')
    normalized_text = re.sub(r'[^a-z0-9_]', '', ascii_text)
    return normalized_text

def add_file_extension(filename_no_extension, extension):
    #clean_name = normalize_text(text)
    return f"{filename_no_extension}.{extension}"

def create_file_path(folder, filename_no_extension, extension):
    filename = add_file_extension(filename_no_extension, extension)
    return os.path.join(folder, filename)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')