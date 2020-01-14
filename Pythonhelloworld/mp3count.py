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
myPath = config['mp3count']['path']
#print(myPath)
# get a searchString from the config file
searchString = config['mp3count']['searchString']

# check if username needs to be replaced with the OS username
if "$USER" in myPath:
    myPath = myPath.replace("$USER", user)
    print(f"Path to use = {myPath}")

# specifically check for mp3
mp3Counter = len(glob.glob1(myPath,"*.mp3"))

# find number of files/dirs in parent directory
count = len([f for f in os.listdir(myPath) ])
if count > 0:
    print(f"Number of items in parent dir = {count}")

# find number of mp3 files in parent directory
count = len([f for f in os.listdir(myPath)
            if f.endswith('.mp3') and os.path.isfile(os.path.join(myPath, f))])
if count > 0:
    print(f"Number of mp3 files in parent dir = {count}")

# count all files
file_count = sum((len(f) for _, _, f in os.walk(myPath)))
print("Total file count = {}".format(file_count))

#TODO get the extension types from config file
mp3_count = 0
other = 0
for root, dirs, files in os.walk(myPath):
    for file in files:
        if file.lower().endswith('.mp3'):
            mp3_count += 1
        else:
            other += 1
print("MP3 file count = {}".format(mp3_count))
print("other file count = {}".format(other))

mp3_count = 0
jpg_count = 0
m4a_count= 0
other_count = 0
hit_count = 0
for root, dirs, files in os.walk(myPath):
    for file in files:
        filename, file_extension = os.path.splitext(file)
        if searchString in filename:
            hit_count += 1
        if file_extension.lower() == '.mp3':
            mp3_count += 1
        elif file_extension.lower() == '.jpg':
            jpg_count += 1
        elif file_extension.lower() == '.m4a':
            m4a_count += 1
        else:
            other_count += 1
            #if file_extension != '.au':
            #    print(file_extension)
            #print(file)
media_count = mp3_count + jpg_count + m4a_count + other_count
print("MP3/JPG/M4A/Other file count = {0} + {1} + {2} + {3} = {4}".format(mp3_count, jpg_count, m4a_count, other_count, media_count))


arr_txt = [x for x in os.listdir(myPath) if searchString in x]
print("Directories containing '{}' = {}".format(searchString, arr_txt))

# searchString
print("Number of files containing '{}' : {}".format(searchString, hit_count))

#x = [os.path.join(r,file) for r,d,f in os.walk(myPath) for file in f if file.endswith(".au")]
#print(x)
