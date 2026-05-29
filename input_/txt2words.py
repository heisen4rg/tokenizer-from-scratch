import os

def load_file(file_path):
    file_path = os.path.abspath(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().lower()
        return content