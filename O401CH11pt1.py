# Python Script
# Part 1 - Ops401
# Marcus Miles
# Script Function: Scans Various Ports on the Host Network and sends Input

# Importing IP address
from ipaddress import IPv4Network

# Importing ICMP, IP , etc
import scapy.all as S
from scapy.all import ICMP, IP, sr1, TCP

# Importing Random
import random

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

# End of Script
