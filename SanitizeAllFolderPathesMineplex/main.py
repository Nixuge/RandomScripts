import os

GOOD_LETTERS = "abcdefghijklmnopqrstuvwxyz0123456789()._"
def sanitize(text: str):
    newText = ""
    for char in text.lower():
        if char in GOOD_LETTERS:
            newText += char
    
    return newText

SUBSTITUTION_REPLACEMENTS = {
    " - Base": "_base",
    " - Bridges": "_bridges"
}

FULL_REPLACEMENTS = {
    "mineplexbackup": "zip",
    "nanogames": "nano"
}

BASE_PATH = "/home/nix/coding/Vue/vue-mpback-test/dist/static/"
def sanitize_entire_folder(folderpath: str):
    for file in os.listdir(folderpath):
        newFileName = file
        for key, substitution in SUBSTITUTION_REPLACEMENTS.items():
            if key in file:
                newFileName = file.replace(key, substitution)

        newFileName = sanitize(newFileName)

        if newFileName in FULL_REPLACEMENTS.keys():
            newFileName = FULL_REPLACEMENTS[newFileName]
        
        os.rename(f"{folderpath}/{file}", f"{folderpath}/{newFileName}")
        if os.path.isdir(f"{folderpath}/{newFileName}"):
            sanitize_entire_folder(f"{folderpath}/{newFileName}")


if __name__ == "__main__":
    sanitize_entire_folder(BASE_PATH)