#one way is to do the listdir method
#[d for d in os.listdir(dirname) if os.path.isdir(os.path.join(dirname,d))]

#use os.walk
#next(os.walk('.'))[1]
#os.walk is a generator and calling next will get the first result in the form of a 3-tuple (dirpath, dirnames, filenames). Thus the [1] index returns only the dirnames from that tuple.

#use scandir
#[f.path for f in os.scandir('E:\mp3') if f.is_dir() ]

#use pathlib
#[f for f in Path('E:\mp3').iterdir() if f.is_dir()]
import glob
from pathlib import Path
import sys

def calculate_size(folder):
    totalsize=0
    for file in Path(folder).glob('*'):
        totalsize = totalsize + int(Path.lstat(file).st_size)
    print(f"{folder} :{totalsize/1024/1024/1024:.2f} GB")

if __name__=='__main__':
    dirname = sys.argv[1]
    list_dirs=[]
    subfolders = [f for f in Path(dirname).iterdir() if f.is_dir()]
    for folder in subfolders:
        calculate_size(folder)
    print("-"*50)
    # list_dirs.append((folder, totalsize))
    # list_sorted = sorted(list_dirs, key=lambda item: item[1], reverse=True)
    # for item in list_sorted:
    #     print (f"{item[0]}: {item[1]/1024/1024/1024:.2f} GB")
