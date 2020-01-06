import os
from os import listdir
from os.path import isfile, join
import datetime
from argparse import ArgumentParser

# command line parameters
parser = ArgumentParser()
parser.add_argument("-d", "--dir", dest="directory",
                    help="The directory to read", metavar="DIR")
parser.add_argument("-t", "--top", dest="top", type=int,
                    help="the top number of file types", metavar="TOP")
parser.add_argument("-q", "--quiet",
                    action="store_false", dest="verbose", default=True,
                    help="don't print status messages to stdout")
args = parser.parse_args()

# get the path from command line (default is current directory)
mypath = "."
if args.directory != None:
    mypath = args.directory

# get the top n from command line (default is top 5)
top = 5
if args.top != None:
    top = args.top

start = datetime.datetime.now()
d = {}

# recursively walk the way
for root, dirs, files in os.walk(mypath):
    for file in files:
        _ , file_extension = os.path.splitext(file)
        if file_extension in d.keys():
            d[file_extension] += 1
        else:
            d[file_extension] = 1

# Sort the results
sorted_d = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
print(f"sorted totals per extension: {sorted_d[:top]}")

# print the top n, now with print formatting and alighment
print(f"path = {mypath} checking for top {top} file extensions")
i = 0
for f in sorted_d:
    if i < top:
        i += 1
        print(f"#{i}    {f[0]:{10}}   {f[1]:{10}} ")

# other calculations
print(f"total number of files in this path: {sum(d.values())}")
end = datetime.datetime.now()
delta = end - start
#print(delta)
elapsed_time = int(delta.total_seconds() * 1000)
print("elapsed_time: {} milliseconds.".format(elapsed_time))
