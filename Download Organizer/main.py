import os
import shutil

BASE_PATH = "/home/nix/Downloads/"
EXTENSION_TABLE = {
    "archives": ["zip", "7z", "rar", "gz", "zst", "bz2", "tar", "deb", "nupkg"],
    "jars": ["jar", "litemod"],
    "text": ["txt", "json"],
    "torrent": ["torrent"],
    "executables": ["appimage", "exe", "msi"],
    "images": ["png", "jpg", "jpeg", "webp", "gif", "svg", "ico"],
    "pdf": ["pdf"],
    "scripts": ["py", "sh", "bash", "run"],
    "documents": ["docx", "doc", "odt", "pptx", "ods", "xlsx", "csv", "odp"],
    "web": ["html", "js", "css"],
    "media": ["mp4", "mkv", "m3u", "m3u8", "mp3", "mov", "webm", "ts"],
    "iso": ["iso", "wbfs", "3ds"],
    "osu": ["osz", "osr", "osk"],
    "android": ["apk"],
    "ios": ["ipa", "mobileconfig", "shsh", "shsh2"],
    "font": ["ttf"],
    "various": ["reg", "atom", "gpg", "fd", "elf", "shortcut", "dat", "pom", "pem", "mrpack", "dll"],

    "no extension": ["EMPTY"]
}


def move_to_folder(file: str, subfolder: str):
    if not subfolder[-1] == "/":
        subfolder += "/"

    if not os.path.isdir(BASE_PATH + subfolder):
        if os.path.exists(BASE_PATH + subfolder):
            print("Subfolder is a file. Exiting")
            return

        os.mkdir(BASE_PATH + subfolder)

    shutil.move(BASE_PATH + file, BASE_PATH + subfolder + file)
    print("moved file " + file + " to subfolder " + subfolder)
        


def main():
    for file in os.listdir(BASE_PATH):
        full_path = BASE_PATH + file
        if os.path.isdir(file):
            move_to_folder(file, "folders")
            continue
            
        extension = file.split('.')[-1]
        if extension != None and extension != "" and '.' in file:
            extension = extension.lower()
        elif os.path.isdir(full_path):
            extension = "FOLDER"
        else:
            extension = "EMPTY"
        
        for subfolder, extensions in EXTENSION_TABLE.items():
            if extension in extensions:
                move_to_folder(file, subfolder)
            

if __name__ == "__main__":
    main()