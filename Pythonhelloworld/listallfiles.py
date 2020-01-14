import os
from os import listdir
from os.path import isfile, join
from argparse import ArgumentParser
import time

# command line parameters
parser = ArgumentParser()
parser.add_argument("-d", "--dir", dest="directory",
                    help="The directory to read", metavar="DIR")
parser.add_argument("-q", "--quiet",
                    action="store_false", dest="verbose", default=True,
                    help="don't print status messages to stdout")
args = parser.parse_args()

# get the path from command line (default is current directory)
mypath = "."
if args.directory != None:
    mypath = args.directory

start = time.time()
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print('files are {}'.format(onlyfiles))
elapsed_time = int(time.time() - start)
print("elapsed_time: {}".format(elapsed_time))
