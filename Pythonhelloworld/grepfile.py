import os
import sys
import re
from argparse import ArgumentParser

# command line parameters
parser = ArgumentParser()
parser.add_argument("-d", "--dir", dest="directory",
                    help="The directory to read", metavar="DIR")
parser.add_argument("-n", "--name", dest="name",
                    help="file name or part of it", metavar="NAME")
parser.add_argument("-g", "--grep", dest="grep",
                    help="regex to grep", metavar="GREP")
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
searchpattern = args.grep
print(f"In '{dir_path}' looking in file '{name}' for '{searchpattern}'")

# grep
with open(args.name) as origin_file:
    for line in origin_file:
        found = re.findall(r(searchpattern), line)
        if found:
            print(f"Match:: {line}")
            #line = line[0].split('"')[1]
            #print(line)
