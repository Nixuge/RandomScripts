import os
import shutil

RECURSIVE = False
GOOD_LETTERS = "abcdefghijklmnopqrstuvwxyz0123456789()._"

def sanitize(text: str):
    newText = ""
    for char in text.lower():
        if char in GOOD_LETTERS:
            newText += char
    
    return newText

def run_folder(path: str):
    for file in os.listdir(path):
        new_filename = sanitize(file)
        if file != new_filename:
            shutil.move(file, new_filename)
        
        if RECURSIVE and os.path.isdir(new_filename):
            run_folder(f"{path}/{new_filename}")

if __name__ == "__main__":
    run_folder('.')