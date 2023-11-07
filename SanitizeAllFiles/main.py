#!/bin/sh
import os
import shutil

RECURSIVE = True
GOOD_LETTERS = "abcdefghijklmnopqrstuvwxyz0123456789()._"

def sanitize(text: str):
    newText = ""
    for char in text.lower():
        if char in GOOD_LETTERS:
            newText += char
        elif char in "éè":
            newText += "e"
    
    return newText

def run_folder(path: str):
    for file in os.listdir(path):
        new_filename = sanitize(file)
        if file != new_filename:
            print(f"Renamed file {file} to {new_filename}")
            shutil.move(f"{path}/{file}", f"{path}/{new_filename}")
        
        if RECURSIVE and os.path.isdir(f"{path}/{new_filename}"):
            run_folder(f"{path}/{new_filename}")

if __name__ == "__main__":
    run_folder('.')