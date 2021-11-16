# Python Script - Antivirus Tool
# Part 2 - Ops401
# Marcus Miles

import os
import hashlib
import time


# Fetching directory and file name
direc = input ("Please type in a directory: ")
filename = input ("Please type in a file name: ")
# Changing directory
os.chdir(direc)
# Simple if else to detect virus file
if (filename) in (direc) == ('virus.exe'):
    print ("Virus exe file has been found")
else:
    print ("No virus exe file has been found")
# Printing all files in the respective directory
path = '(direc)'

files = os.listdir(path)

for f in files:
	print(f)

# Variable for file size
file_size = os.path.getsize(filename)

# Variable for time
timestamp=time.time

# Function 1 - Gets MD5 hash value from file
def md5():
    hashlib.md5(filename).hexdigest()
md5()
print("Path",(direc))
print("Name",(filename))
print("Size",(file_size))
print("Time",(timestamp))

# End
