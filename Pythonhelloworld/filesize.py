import os
from argparse import ArgumentParser

# command line parameters
parser = ArgumentParser()
parser.add_argument("-d", "--dir", dest="directory",
                    help="The directory to read", metavar="DIR")
parser.add_argument("-l", "--limit", dest="limit", type=int,
                    help="file size limit in bytes", metavar="LIMIT")
parser.add_argument("-q", "--quiet",
                    action="store_false", dest="verbose", default=True,
                    help="don't print status messages to stdout")
args = parser.parse_args()

# function to get the right units
def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

# function to retrieve file size with size units
def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)

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

# check file_size
file_path = r"C:\Windows\System32\mspaint.exe"
size = file_size(file_path)
print(size)

# check file_bytesize
file_path = r"C:\Windows\System32\mspaint.exe"
size = file_bytesize(file_path)
print(size)

# get the path from command line (default is current directory)
dir_path = "."
if args.directory != None:
    dir_path = args.directory

# get the limit from command line (default is 1 kB)
limit = 1024
if args.limit != None:
    limit = args.limit
print(f"dir_path = {dir_path} checking for limit {limit}")

# go through all files
for r, d, f in os.walk(dir_path):
    for file in f:
        file_path = os.path.join(dir_path,file)
        #print(file_path)
        size = file_bytesize(file_path)
        if size != None and size > limit:
            print(f"file size {size:{10}} > {limit} bytes for {file}")
#        else:
#            print(f"file size {size}")

## # TODO: read the filenames from input file and loop through
## # TODO: totals per Directory
