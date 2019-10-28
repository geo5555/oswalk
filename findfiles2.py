import pathlib

count=0

for p in pathlib.Path("e:\mp3").rglob("*.mp3"):
    print(p)
    print(type(p))
    count +=1

print(count)