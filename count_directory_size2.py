import os, fnmatch
import sys
from pathlib import Path
import itertools
import operator

totalsize=0
subtotal=0
count=0
list_dirs = []
#for path, dirs, files in os.walk(r"D:\000WEB PROGRAMMING"):
for path, dirs, files in os.walk(sys.argv[1]):
    #print("path="+path)
    directorysize=0
    if len(files)>0:
        for name in files:
            if fnmatch.fnmatch(name, '*'):
                filename = os.path.join(path, name)
                filesize = os.path.getsize(filename)
                totalsize = totalsize + filesize
                count += 1
                directorysize += filesize
        list_dirs.append((path, directorysize)) 
        print(f"{path} : {directorysize/1024/1024:.2f} Mbytes")
        
# print(f"totalsize in bytes: {totalsize:.2f}")
# print(f"totalsize in Mbytes: {totalsize/1024/1024:.2f}")
# print(f"totalsize in Gbytes: {totalsize/1024/1024/1024:.2f}")
# print(f"number of files: {count}")
# print("*"*50)
# list_sorted = sorted(list_dirs, key=lambda item: item[1], reverse=True)
# for item in list_sorted:
#     if item[1]>0:
#         print (f"{item[0]}: {item[1]/1024/1024:.2f} MB")

def accumulate(l):
    it = itertools.groupby(l, operator.itemgetter(0))
    for key, subiter in it:
       yield key, sum(item[1] for item in subiter) 

print("*"*50)
level=4
list_levels=[]
for path,size in list_dirs:
    parts = (Path(path).parts)
    if len(parts)>=level:
        root = parts[0]
        for l in range(level):
                l1=Path(root).joinpath(parts[l])
                root = l1
        print(l1)
        list_levels.append((str(l1), size))
print("*"*100)
print(list(accumulate(list_levels)))

