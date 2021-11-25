# Python Script
# Marcus Miles
# Importing the correct os library
import os

# First 4 functions - 2 modes

### Mode 1 ###
def mode1():
    urlorip=input("Enter Target IP or URL: ")
    
### Mode 2 ###
def mode2():
    port=input("Enter Target Port Number: ")
  
### Mode 3 telnet ###
def teln():
    query=('teln ' +  mode1() + ' '+ mode2())
    print("Control + ]'and control + D' to exit telnet")
    return os.system(query)
### Mode 4 netcat ###
def netcat():
    query=('nc -N ' +  mode1() + ' '+ mode2())
    print("***Press 'CTL + D' To Exit NETCAT Session***")
    return os.system(query)
### Mode 5 nmap ###
def nmapmode():
    query=('nmap -F ' + mode1())
    return os.system(query)
### Menu ###
def menu():
  # Short while loop to make the script easier to use
    while True:
        mode = input("""
        Banner Grabbing Tool
        Mode 1
        Mode 2
        Nmap
        Exit
        What mode do you want? Enter mode name not number: 
        """)

        if mode=="mode1":
            mode1()
        if mode=="mode2":
            mode2()
        if mode=="nmap":
            nmapmode()
        if mode=="exit":
            print ("Control + c")
        else:
            print ("Wrong mode")

# End Script


       

