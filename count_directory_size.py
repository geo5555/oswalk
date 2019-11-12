import os, fnmatch
import sys

totalsize=0
count=0
list_dirs = []
#for path, dirs, files in os.walk(r"D:\000WEB PROGRAMMING"):
for path, dirs, files in os.walk(sys.argv[1]):
    #print("path="+path)
    directorysize=0
    for name in files:
        if fnmatch.fnmatch(name, '*'):
            filename = os.path.join(path, name)
            filesize = os.path.getsize(filename)
            totalsize = totalsize + filesize
            count +=1
            directorysize+= filesize
    list_dirs.append((path, directorysize))    
    print(f"path={path}, directorysize={directorysize/1024/1024:.2f} Mbytes")

print(f"totalsize in bytes: {totalsize:.2f}")
print(f"totalsize in Mbytes: {totalsize/1024/1024:.2f}")
print(f"totalsize in Gbytes: {totalsize/1024/1024/1024:.2f}")
print(f"number of files: {count}")
# list_sorted = sorted(list_dirs, key=lambda item: item[1], reverse=True)
# for item in list_sorted:
#     if item[1]>0:
#         print (f"{item[0]}: {item[1]/1024/1024:.2f} MB")
