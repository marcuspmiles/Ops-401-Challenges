# Python Script
# Ops 401 - Challenge 1

# Script transmits a single ICMP packet to a specific IP every two seconds

import os
hostname = "8.8.8.8" 
response = os.system("ping -D -i 2 " + hostname)

if response == 0:
  print ('Failed')
else:
  print ('Success')
