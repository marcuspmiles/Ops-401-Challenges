# Python Script - Antivirus Tool
# Part 3 - Ops401
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

# Virus Total Check Hash Function
def checkhash(chash):
	try:
		if len(chash) == 32:
			return chash
		elif len(chash) == 40:
			return chash
		elif len(chash) == 64:
			return chash
		else:
			print ("Your HASH must have 32, 40 or 64 Alpha Numeric characters.")
			exit()

	except Exception as Error:
			print(Error)
# Virus Total Check Key Function
def checkkey(ckey):
	try:
		if len(ckey) == 64:
			return ckey
		else:
			print("Your VirusTotal API must have 64 Alpha Numeric characters.")
			exit()

	except Exception as Error:
			print(Error)
checkhash()
md5()
# End
