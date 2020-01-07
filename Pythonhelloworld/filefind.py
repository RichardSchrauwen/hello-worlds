import os
import sys
from argparse import ArgumentParser

# command line parameters
parser = ArgumentParser()
parser.add_argument("-d", "--dir", dest="directory",
                    help="The directory to read", metavar="DIR")
parser.add_argument("-n", "--name", dest="name",
                    help="file name or part of it", metavar="NAME")
parser.add_argument("-q", "--quiet",
                    action="store_false", dest="verbose", default=True,
                    help="don't print status messages to stdout")
args = parser.parse_args()

# get the path from command line (default is current directory)
dir_path = "."
if args.directory != None:
    dir_path = args.directory

# get the file name from command line
if args.name == None:
    print("Oops, no file name was entered. Please use '-n <name>' arg.")
    sys.exit()
name = args.name
print(f"In '{dir_path}' looking for file containing '{name}'")

# go through all files
for r, d, f in os.walk(dir_path):
    for file in f:
        if name and name in file:
            file_path = os.path.join(r,file)
            print(f"Found under file path {file_path}")
