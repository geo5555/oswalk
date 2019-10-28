import glob
from pathlib import Path

count=0
totalsize=0

for file1 in glob.glob('e:\mp3/**/*.mp3', recursive=True):
    print(file1)
    #print(type(file1)) this is type string, I cannot call lstat on it.
    #totalsize = totalsize + int(Path.lstat(file1).st_size)
    count +=1

print(f"totalsize in bytes: {totalsize}")
print(f"totalsize in Mbytes: {totalsize/1024/1024}")
print(f"totalsize in Gbytes: {totalsize/1024/1024/1024}")
print(f"number of files: {count}")

#files=Path('e:\mp3').glob('**/*.mp3') OK
#files = glob.glob('e:/mp3/*.mp3', recursive=True) #this does not work recursive
#files = glob.glob('e:\mp3\**\*.mp3', recursive=True) OK with recursive, with no recursive returns less files