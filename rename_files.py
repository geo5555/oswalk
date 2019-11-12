import glob
from pathlib import Path
import re
import argparse

<<<<<<< HEAD
#file.rename without full path in rename moves the file to the directory
#where you execute the command

count_affected=0
count_will_be_affected=0
=======
count_affected = 0
count_will_be_affected = 0
>>>>>>> b72018f61fa08c2a682c97957461b7b78d84c8e7

parser = argparse.ArgumentParser(
    description="rename or delete files based on extension and pattern"
)

parser.add_argument('directory', action="store", help="starting directory")
parser.add_argument('-a', '--action', action="store",
                    choices=["rename", "delete"], default="rename", help="rename files")
parser.add_argument('-del', '--delete', action="store_true",
                    help="delete files matching pattern")
parser.add_argument('-r', '--recursive', action="store_true",
                    help="recursive or only this directory")
parser.add_argument('-ext', '--extension', action="store",
                    help="search files with this extension only")
parser.add_argument('-p1', '--pattern', action="store",
                    help="pattern to search files for")
parser.add_argument('-p2', '--replace_pattern',
                    action="store", default='', help="rename files")
parser.add_argument('-dry', '--dryrun', action="store_true",
                    help="do not change files, dry run")
parser.add_argument('-esc', '--escape', action="store_true",
                    help="escape special character or not")

# Parse the arguments
args = parser.parse_args()
if args.extension is None:
    parser.error('-ext extension is required')
if args.pattern is None:
    parser.error('-p1 required')
if args.recursive:
    extension = "**/*."+args.extension
else:
    extension = "*."+args.extension

if args.escape:
    pattern = re.escape(args.pattern)
    # re.escape escapes with \ all non alphanumeric characters
else:
    pattern = args.pattern

for file in Path(args.directory).glob(extension):
    filename = file.name
    if re.search(pattern, filename, flags=re.I):
        count_will_be_affected += 1
        if args.action == "rename":
            result = re.sub(pattern, args.replace_pattern,
                            filename, flags=re.I)
            if not args.dryrun:
                try:
<<<<<<< HEAD
                    file.rename(file.parent.joinpath(result)) 
                    #without joinpath moves the file to another dir
                    print(f"{filename} => {result}")
                    count_affected+=1
                except FileExistsError:
                    print(result+" already exists")
            else:
                print(f"{filename} | will be renamed to | {result}")
        elif args.action=="delete":
=======
                    file.rename(file.parent.joinpath(result))
                    # if I dont specify full path the file will be created in the directory where I run the script
                    # so it will be moved to the new directory with the new name
                    print(f"{file} renamed to {file.parent.joinpath(result)}")
                    count_affected += 1
                except FileExistsError:
                    print(result+" already exists")
            else:
                print(f"{file} will be renamed to {file.parent.joinpath(result)}")
        elif args.action == "delete":
>>>>>>> b72018f61fa08c2a682c97957461b7b78d84c8e7
            if not args.dryrun:
                try:
                    file.unlink()
                    print(f"{filename} is deleted")
                    count_affected += 1
                except PermissionError:
                    print(f"no permission to delete file {filename}")
            else:
                print(f"{filename} - will be deleted")


if not args.dryrun:
    print(f"files affected: {count_affected}")
else:
    print(f"files that will be affected: {count_will_be_affected}")
