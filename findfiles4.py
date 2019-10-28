import glob
from pathlib import Path
import re

count=0
totalsize=0

for file in Path('e:\mp3').glob('**/*.mp3'):
    #print(file)
    #print(type(file1))  class pathlib.windowspath
    totalsize = totalsize + int(Path.lstat(file).st_size)
    count +=1

print(f"totalsize in bytes: {totalsize}")
print(f"totalsize in Mbytes: {totalsize/1024/1024}")
print(f"totalsize in Gbytes: {totalsize/1024/1024/1024}")
print(f"number of files: {count}")
