import glob
from pathlib import Path
import re

count=0
totalsize=0

for file in Path('D:\downloads\music').glob('**/*.mp3'):
    filename = str(file)
    if (re.search(r'\[mp3clan\.com\]', filename)):
        result = re.sub(r'\[mp3clan\.com\]', '', filename)
        try:
            file.rename(result)
            print(f"{filename} renamed to {result}")
            count +=1
        except FileExistsError:
            print(result+" already exists")


print(f"renamed: {count}")
