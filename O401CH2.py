# Python Script
# Ops 401 - Challenge 1
# Ops 401 Challenge 2 - Build from Challenge 1

# Script transmits a single ICMP packet to a specific IP every two seconds
# Script sends an email to admin if host changes from up to down

# Importing Mail Module
import smtplib
# Importing OS Module
import os
hostname = "8.8.8.8" 
response = os.system("ping -D -i 2 " + hostname)
# If - else statement for status up or status down
if response == 0:
  print ('%%%Status - Down%%%')
else:
  print ('%%%Status-Up%%%')
# If - else statement to send email on status change

if response == 0:
        sender = 'from@fromdomain.com'
receivers = ['marcuspmiles@gmail.com']

message = """From: Test <from@fromdomain.com>
To: To Person <marcuspmiles@gmail.com>
Subject: SMTP e-mail test

reponse: (response)
Host just changed from "up" to "down"
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")

# End
