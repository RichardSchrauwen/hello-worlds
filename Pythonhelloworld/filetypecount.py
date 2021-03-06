import glob
import configparser
import re
import os
from os import listdir
from os.path import isfile, join

# get user logged in
user = os.getlogin()
#print(user)

# get path and searchString from the INI config file
config = configparser.ConfigParser()
config.read('example.ini')
myPath = config['filetypecount']['path']
searchExtension = config['filetypecount']['searchExtension']
searchString = config['filetypecount']['searchString']
#print(f"searchString = '{searchString}'")

# check if username needs to be replaced with the OS username
if "$USER" in myPath:
    myPath = myPath.replace("$USER", user)
    print(f"Path to use = {myPath}")

# count all files
file_count = sum((len(f) for _, _, f in os.walk(myPath)))
print("Total file count for {0} = {1}\n".format(myPath, file_count))

string_count = 0
extension_count = 0
other_count = 0

# recursively walk the way
for root, dirs, files in os.walk(myPath):
    for file in files:
        if searchString and searchString is not None and searchString in file:
            string_count += 1
        filename, file_extension = os.path.splitext(file)
        if file_extension.lower() == searchExtension:
            extension_count += 1
        else:
            other_count += 1

# print results
file_count = extension_count + other_count
print("file count : {0} ({3}) + {1} (other) = {2}".format(extension_count, other_count, file_count, searchExtension))
#print("file count with extension '{0}' = {1}".format(searchExtension, extension_count))
print("file count containing '{0}' = {1}".format(searchString, string_count))
