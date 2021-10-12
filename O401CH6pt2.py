# Python Script - Marcus Roxburgh Miles
# Encrypts, Decrypts text and files

# Importing OS
import os.path
# Importing Fernet
from cryptography.fernet import Fernet

# User options
print ("%%%%%%%%% FILE AND MESSAGE DECRYPTER / ENCRYPTER %%%%%%%%%")
print ("Encrypt a file (mode1)")
print ("Decrypt a file (mode2)")
print ("Encrypt a message (mode3)")
print ("Decrypt a message (mode4)")
print ("Recursively encrypt a folder (mode5)")
print ("Recursively decrypt a folder (mode6)")
user_prompt = input("What would you like to do? TYPE THE MODE: ")

##
# Function to encrypt a file
##
def encrypt(filename, key):
    f = Fernet(key)
##
# Function to decrypt a file 
##
def decrypt(filename, key):
    f = Fernet(key)
##
# Function to write a key
##
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
##
# Function to load that key
##
def load_key():
    return open("key.key", "rb").read()

############### MODE 1 #################

if (user_prompt) == ('mode1'):
   # Writing the key
   write_key()
   key = load_key()
   f = Fernet(key)
   # Asking for file input
   filename = input("Please type a file to encrypt: ")
  with open((filename), "rb") as file:
       file_data = file.read()
       # Reads file data
       encrypted_data = f.encrypt(file_data)
       # Encrypts the file
   with open((filename), "wb") as file:
       file.write(encrypted_data)

############### MODE 2 #################
 
if (user_prompt) == ('mode2'):
   # Writing the key
   write_key()
   key = load_key()
   f = Fernet(key)
   # Asking for file input
   filename = input("Please type a file to decrypt: ")
   with open((filename), "rb") as file:
       file_data = file.read()
       encrypted_data = f.encrypt(file_data)
   # Decryptes the file
       decrypted_data = f.decrypt(encrypted_data)
   with open((filename), "wb") as file:
       file.write(decrypted_data)
      
############### MODE 3 #################
 
if (user_prompt) == ('mode3'):
   # Writing the key, loading the key, and attatching a message to that key
   write_key()
   key = load_key()
   # Encoding and ecnrypting the key
   message = input("Type a message to encrypt: ") .encode()
   f = Fernet(key)
   encrypted = f.encrypt(message)
   # Shows encrypted message in encoded form
   print ("%%%%Encrypted Message%%%%")
   print(encrypted)
else:
   print ("---")

############### MODE 4 #################

if (user_prompt) == ('mode4'):
   # Writing the key, loading the key, and attatching a message to that key
   write_key()
   key = load_key()
   # Encoding and ecnrypting the key
   message = input("Input message to decrypt: ") .encode()
    f = Fernet(key)
   encrypted = f.encrypt(message)
   # Decrypts message
   decrypted_encrypted = f.decrypt(encrypted)
   # Shows decrypted message in decoded form
   print ("%%%%Decrypted Messsage%%%%")
   print(decrypted_encrypted)
else:
   print ("---")

############### MODE 5 #################

if (user_prompt) == ('mode5'):
   # Recursively walking all folders and extensions
   topdir = '.'
   exten = ''
   for dirpath, dirnames, files in os.walk(topdir):
      for name in files:
         if name.lower().endswith(exten):
            print(os.path.join(dirpath, name))
   # Writing the key
   write_key()
   key = load_key()
   f = Fernet(key)
   # Asking for file input
  foldername = input("Please type a folder to recursively encrypt: ")
   with open((foldername), "rb") as folder:
       folder_data = folder.read()
       # Reads file data
       encrypted_data = f.encrypt(folder_data)
       # Encrypts the file
   with open((foldername), "wb") as folder:
       folder.write(encrypted_data)

############### MODE 6 #################

if (user_prompt) == ('mode6'):
   # Recursively walking all folders and extensions
   topdir = '.'
   exten = '.dir'
   for dirpath, dirnames, files in os.walk(topdir):
      for name in files:
         if name.lower().endswith(exten):
            print(os.path.join(dirpath, name))
   # Writing the key
   write_key()
   key = load_key()
   f = Fernet(key)
   # Asking for file input
   filename = input("Please type a folder to recursively decrypt: ")
    with open((filename), "rb") as file:
       file_data = file.read()
       encrypted_data = f.encrypt(file_data)
   # Decryptes the file
       decrypted_data = f.decrypt(encrypted_data)
   with open((filename), "wb") as file:
       file.write(decrypted_data)

# End of Script
