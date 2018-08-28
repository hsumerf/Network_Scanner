#It will broadcast the IP address and ask who has this IP adress
#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    #arp_request.pdst=ip
    print(arp_request.summary())
    # scapy.ls(scapy.ARP())

scan("172.17.0.1/24")

