import os
from argparse import ArgumentParser

# command line parameters
parser = ArgumentParser()
parser.add_argument("-d", "--dir", dest="directory",
                    help="The directory to read", metavar="DIR")
parser.add_argument("-e", "--ext", dest="extension",
                    help="The extenstion type to look for", metavar="EXT")
parser.add_argument("-q", "--quiet",
                    action="store_false", dest="verbose", default=True,
                    help="don't print status messages to stdout")
args = parser.parse_args()

# get the path from command line (default is current directory)
mypath = "."
if args.directory != None:
    mypath = args.directory

# get the extension from command line (default is empty)
myext = ""
if args.extension != None:
    myext = args.extension

# list all files and send output to a file
with open("myfiles.txt", "w", encoding="utf-8") as filewrite:
    # recursively walk the way
    for root, dirs, files in os.walk(mypath):
        for file in files:
            _ , file_extension = os.path.splitext(file)
            if file_extension == myext:
                filewrite.write(f"{root + file}\n")
