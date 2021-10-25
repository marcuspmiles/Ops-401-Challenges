# Python Script
# Ops401 - Challenge 16 - 10-25-21
# Marcus Miles

# Importing Specific Libraries
import time, getpass

###### FUNCTION 1 ######
def offensive ():
    filepath = input("Enter your filepath:\n")
    print(filepath)
    # Opening the file and encoding
    file = open(filepath, encoding = "ISO-8859-1")
    line = file.readline()
    # While loop to set delay
    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close()
    # Printing the var
    print(line)
#######################

###### FUNCTION 2 ######
def defensive ():
   string = input("Please enter a string: ")
   wordfpath = input("Please enter a word list filepath: ")
   file = open(wordfpath, encoding = "ISO-8859-1")
   line = file.readline()
   while line:
      line = line.rstrip()
      string = line
      print(string)
      line = file.readline()
   file.close()
   print(string)
########################

###### MENU ######
menu = input("""
Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Exit
    Please enter a number:
""")
if (menu == "1"):
    offensive()
elif (menu == "2"):
    defensive()
elif (menu == "3"):
    print ("Type CTRL + C")
else:
    print ("Type something Else")
##################

  
