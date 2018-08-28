#Asking who has this MAC address
#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    #IP packet
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    #Asking who has this MAC address
    #1
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()
    #2
    # broadcast = scapy.Ether()
    # broadcast.dst = "ff:ff:ff:ff:ff:ff"
    #print(broadcast.summary())

    #combining both packets
    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()

scan("172.17.0.1/24")

