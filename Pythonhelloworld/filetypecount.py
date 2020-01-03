import glob
import configparser
import re
import os
from os import listdir
from os.path import isfile, join

# get user logged in
user = os.getlogin()
#print(user)

# get path from the config file
config = configparser.ConfigParser()
config.read('example.ini')
myPath = config['filetypecount']['path']

# check if username needs to be replaced with the OS username
if "$USER" in myPath:
    myPath = myPath.replace("$USER", user)
    print(f"Path to use = {myPath}")

# count all files
file_count = sum((len(f) for _, _, f in os.walk(myPath)))
print("Total file count = {}".format(file_count))

# count a specific file_extension type
extension_count = 0
other_count = 0
for root, dirs, files in os.walk(myPath):
    for file in files:
        filename, file_extension = os.path.splitext(file)
        if file_extension.lower() == '.mp3':
            extension_count += 1
        else:
            other_count += 1

file_count = extension_count + other_count
print("file count : {0} + {1} = {2}".format(extension_count, other_count, file_count))

# get a searchString from the config file
searchString = config['filetypecount']['searchString']
arr_txt = [x for x in os.listdir(myPath) if searchString in x]
print("Directories containing '{}' = {}".format(searchString, arr_txt))

# searchString
print("File names containing '{}' : {}".format(searchString, hit_count))

#x = [os.path.join(r,file) for r,d,f in os.walk(myPath) for file in f if file.endswith(".au")]
#print(x)
