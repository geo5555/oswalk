import collections
from pathlib import Path
c = collections.Counter(p.suffix for p in Path.cwd().iterdir() if p.is_file())
print(c)
c = collections.Counter(p.suffix for p in Path('d:\projects\rename-files').rglob('*.py') if p.is_file())
print(c)
c=collections.Counter([p.suffix for p in Path('e:').rglob("**/*") if p.is_file()])
print(c)