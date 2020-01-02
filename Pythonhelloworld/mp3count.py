import glob
import configparser
import re
import os
from os import listdir
from os.path import isfile, join

# get user logged in
user = os.getlogin()
print(user)

# get path from the config file
config = configparser.ConfigParser()
config.read('example.ini')
myPath = config['mp3count']['path']
print(myPath)

# check if username needs to be replaced with the OS username
if "$USER" in myPath:
    myPath = myPath.replace("$USER", user)
    #myPath = re.sub("$USER", user, myPath)
    print(myPath)

# specifically check for mp3
mp3Counter = len(glob.glob1(myPath,"*.mp3"))

count = len([f for f in os.listdir(myPath)
            if f.endswith('.mp3') and os.path.isfile(os.path.join(myPath, f))])
print(count)

count = len([f for f in os.listdir(myPath) ])
print("Unnested file count = {}".format(count))

file_count = sum((len(f) for _, _, f in os.walk(myPath)))
print("Total file count = {}".format(file_count))

#TODO get the extension types from config file

mp3_count = 0
jpg_count = 0
other = 0
for root, dirs, files in os.walk(myPath):
    for file in files:
        if file.lower().endswith('.mp3'):
            mp3_count += 1
        elif file.lower().endswith('.jpg'):
            jpg_count += 1
        elif not file.lower().endswith('.mp3'):
            other += 1

print("MP3 file count = {}".format(mp3_count))
print("JPG file count = {}".format(jpg_count))
print("other file count = {}".format(other))

arr_txt = [x for x in os.listdir(myPath) if "Gorki" in x]
print("Directories with Gorki = {}".format(arr_txt))

mp3_count = 0
jpg_count = 0
m4a_count= 0
other_count = 0
for root, dirs, files in os.walk(myPath):
    for file in files:
        filename, file_extension = os.path.splitext(file)
        if file_extension.lower() == '.mp3':
            mp3_count += 1
        elif file_extension.lower() == '.jpg':
            jpg_count += 1
        elif file_extension.lower() == '.m4a':
            m4a_count += 1
        else:
            other_count += 1
            if file_extension != '.au':
                print(file_extension)
            #print(file)
media_count = mp3_count + jpg_count + m4a_count + other_count
print("MP3/JPG/M4A/Other file count = {0} + {1} + {2} + {3} = {4}".format(mp3_count, jpg_count, m4a_count, other_count, media_count))

x = [os.path.join(r,file) for r,d,f in os.walk(myPath) for file in f if file.endswith(".au")]
print(x)
