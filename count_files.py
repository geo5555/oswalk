import collections
from pathlib import Path
c = collections.Counter(p.suffix for p in Path.cwd().iterdir())
print(c)
c = collections.Counter(p.suffix for p in Path('E:\mp3').rglob('*.mp3'))
print(c)