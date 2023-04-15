#!/bin/python3

import xml.etree.ElementTree as ET

def split(number, url):
    tree = ET.parse(f'{number}.xml')
    root = tree.getroot()


    fullString = ""
    i = 0
    split = 1

    for child in root:
        fullString += f"https://archive.org/download/{url}/" + child.get("name") + "\n"
        i += 1
        if i == 50:
            with open(f"{number}_{split}.txt", "w") as openF:
                openF.write(fullString)
            i = 0
            split += 1
            fullString = ""
    with open(f"{number}_{split}.txt", "w") as openF:
        openF.write(fullString)

def count():
    numbers = ["1", "2", "3"]
    i = 0
    for num in numbers:
        tree = ET.parse(f'{num}.xml')
        root = tree.getroot()
        for child in root: i += 1
    
    print(i)

count()

split(3, "wiieuroperedump3")