import os
from argparse import ArgumentParser

# command line parameters
parser = ArgumentParser()
parser.add_argument("-d", "--dir", dest="directory",
                    help="The directory to read. Default is current dir.", metavar="DIR")
parser.add_argument("-e", "--ext", dest="extension",
                    help="The extenstion type to look for. Wildcard is * for any extension.", metavar="EXT")
parser.add_argument("-l", "--limit", dest="limit", type=int,
                    help="The max file size limit in bytes. Default is 0.", metavar="LIMIT")
parser.add_argument("-q", "--quiet",
                    action="store_false", dest="verbose", default=True,
                    help="don't print status messages to stdout")
args = parser.parse_args()

# get the path from command line (default is current directory)
mypath = "."
if args.directory != None:
    mypath = args.directory

# get the extension from command line (default is empty, Wildcard is * for any extension.)
myext = ""
if args.extension != None:
    myext = args.extension

# get the limit from command line (default is 0 byte, ignore negative values)
limit = 0
if args.limit != None and args.limit > 0:
    limit = args.limit

# output file
myfiles = "myfiles.txt"

print(f"Checking for file type '{myext}' above limit {limit} bytes in {mypath}")

# function to get file size in bytes
def file_bytesize(file_path):
    """
    this function will return the file size in bytes
    """
    if os.path.isfile(file_path):
        #b = os.path.getsize(file_path)
        b = os.stat(file_path).st_size
        if b == None:
            b = 0
        return b

# list all files and send output to a file if conditions match
nr_files = 0
with open(myfiles, "w", encoding="utf-8") as filewrite:
    # recursively walk the way through my path
    for root, dirs, files in os.walk(mypath):
        for file in files:
            if myext != "*":
                _ , file_extension = os.path.splitext(file)
                if file_extension == myext:
                    if limit > 0:
                        file_path = os.path.join(root, file)
                        size = file_bytesize(file_path)
                        if size != None and size > limit:
                            #print(f"file size {size:{10}} > {limit} bytes for {file}")
                            filewrite.write(f"{file_path},{size}\n")
                            nr_files += 1
                    else:
                        filewrite.write(f"{os.path.join(root, file)}\n")
                        nr_files += 1
            else:
                if limit > 0:
                    file_path = os.path.join(root, file)
                    size = file_bytesize(file_path)
                    if size != None and size > limit:
                        filewrite.write(f"{file_path},{size}\n")
                        nr_files += 1
                else:
                    filewrite.write(f"{os.path.join(root, file)}\n")
                    nr_files += 1

print(f"Written {nr_files} file names in {myfiles}")
