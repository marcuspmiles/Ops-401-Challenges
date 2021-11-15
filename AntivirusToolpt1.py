# Python Script - Antivirus Tool
# Part 1 - Ops401
# Marcus Miles

import os

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
