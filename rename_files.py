import glob
from pathlib import Path
import re
import argparse

count=0

parser = argparse.ArgumentParser(
        description="rename or delete files"
    )

parser.add_argument('-a', '--action', action="store", choices=["rename","delete"], default="rename", help="rename files")
parser.add_argument('-del', '--delete', action="store_true", help="delete files matching pattern")
parser.add_argument('-d', '--directory', action="store", help="starting directory")
parser.add_argument('-r', '--recursive', action="store_true", help="recursive or only this directory")
parser.add_argument('-ext', '--extension', action="store", help="search files with this extension only")
parser.add_argument('-p1', '--pattern', action="store", help="pattern to search files for")
parser.add_argument('-p2', '--replace_pattern', action="store", default='', help="rename files")
parser.add_argument('-dry', '--dryrun', action="store_true", help="do not change files, dry run")
parser.add_argument('-esc', '--escape', action="store_true", help="escape special character or not")

# Parse the arguments
args = parser.parse_args()
if args.extension is None:
    parser.error('-ext extension is required')
if args.recursive:
    extension = "**/*."+args.extension
else:
    extension = "*."+args.extension

if args.escape:
    pattern = re.escape(args.pattern)
    #re.escape escapes with \ all non alphanumeric characters
else:
    pattern = args.pattern

for file in Path(args.directory).glob(extension):
    filename = str(file)
    if re.search(pattern, filename, flags=re.I):   
        try:
            if not args.dryrun:
                if args.action=="rename":
                    result = re.sub(pattern, args.replace_pattern, filename, flags=re.I)
                    file.rename(result)
                    print(f"{filename} renamed to {result}")
                elif args.action=="delete":
                    try:
                        file.unlink()
                        print(f"{filename} is deleted")
                    except PermissionError:
                        print(f"no permission to delete file {filename}")
                count+=1
            else:
                if args.action=="rename":
                    result = re.sub(pattern, args.replace_pattern, filename, flags=re.I)
                    print(f"{filename} will be renamed to {result}")
                elif args.action=="delete":
                    print(f"{filename} - will be deleted")
                count +=1
        except FileExistsError:
            print(result+" already exists")


if not args.dryrun:
    print(f"files affected: {count}")
else:
    print(f"files that will be affected: {count}")
