import os, fnmatch
import sys

totalsize=0
count=0

#for path, dirs, files in os.walk(r"D:\000WEB PROGRAMMING"):
for path, dirs, files in os.walk(sys.argv[1]):
    print("path="+path)
    print("files")
    for name in files:
        if fnmatch.fnmatch(name, '*.mp3'):
            filename = os.path.join(path, name)
            print(filename)
            totalsize = totalsize + os.path.getsize(os.path.join(path, name))
            count +=1
        #print(os.path.join(path, name))
        #readTitle(os.path.join(path, name))
    # print("----------------------")
    # print("directories")
    # for name in dirs:
    #     print(os.path.join(path, name))
    #     #pass
    # print("----------------------")

print(f"totalsize in bytes: {totalsize}")
print(f"totalsize in Mbytes: {totalsize/1024/1024}")
print(f"totalsize in Gbytes: {totalsize/1024/1024/1024}")
print(f"number of files: {count}")
