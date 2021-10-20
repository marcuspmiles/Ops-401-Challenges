# Python Script
# Part 3 - Ops401
# Marcus Miles
# Script Function: TCP Port Range Scanner and ICMP Ping Sweeper

# Importing IP address
from ipaddress import IPv4Network

# Importing ICMP, IP , etc
import scapy.all as S
from scapy.all import ICMP, IP, sr1, TCP

# Importing Random
import random

ad_ip = input("Please enter an IP address to target: ")

### Pt 1 ###
def port_sweep(func):

  # Function 1 - Printing Host IP
  s = set()
  for line in S.read_routes():
          s.add(line[4])
  print(" -- HOST IP -- ")
  print(s)

  # Port Range - Printing Port Range
  port_range = [22, 23, 80, 443, 3389]
  print("-- PORT RANGE TO SCAN --")
  print(port_range)

  # TCP - SYN/ACK and RST packets
  host = "127.0.0.1"
  print ("Scanning",(host))

  for dst_port in port_range:
      src_port = random.randint(1025,65534)
      resp = sr1(
          IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,
          verbose=0,
      )

      if resp is None:
          print(f"{host}:{dst_port} is filtered (silently dropped).")

      elif(resp.haslayer(TCP)):
          if(resp.getlayer(TCP).flags == 0x12):
              # Sending an RST to close the connection
              send_rst = sr(
                IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),
                  timeout=1,
                  verbose=0,
              )
              print(f"{host}:{dst_port} is open.")

          elif (resp.getlayer(TCP).flags == 0x14):
              print(f"{host}:{dst_port} is closed.")

      elif(resp.haslayer(ICMP)):
          if(
              int(resp.getlayer(ICMP).type) == 3 and
              int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
          ):
              print(f"{host}:{dst_port} is filtered (silently dropped).")
### Pt 2  ###

# Importing Modules
import subprocess
import ipaddress
import socket

if (ad_ip) == (''):
        # Showing the user current available networks
        print("Current Addresses:")
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print(s.getsockname()[0])
        # Network address input
        network_ad = input("Please enter a network address/CIDR format: ")
        # Finding hosts
        ip_net = ipaddress.ip_network((network_ad), strict =False)
        all_hosts = list(ip_net.hosts())

        info = subprocess.STARTUPINFO()
        info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        info.wShowWindow = subprocess.SW_HIDE
        # Pinging hosts
        for i in range(len(all_hosts)):
                output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_hosts[i])], stdout=subprocess.PIPE,   
        startupinfo=info).communicate()[0]
                # Checking for a response
                if "Destination host unreachable" in output.decode('utf-8'):
                        print(str(all_hosts[i]), "Host is not responding")
                elif "Request timed out" in output.decode('utf-8'):
                        print(str(all_hosts[i]), "Host is not responding")
                else:
                        print(str(all_hosts[i]), "Host is up and responding")
                        func()
# End of Script
