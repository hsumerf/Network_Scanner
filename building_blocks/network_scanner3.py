#Asking who has this MAC address
#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    #IP packet
    arp_request = scapy.ARP(pdst=ip)
    #Asking who has this MAC address
    #1
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #combining both packets
    arp_request_broadcast = broadcast/arp_request
    #srp means send receive packet
    # answered_list,unanswered_list = scapy.srp(arp_request_broadcast,timeout=1)
    answered_list = scapy.srp(arp_request_broadcast,timeout=1)[0]
    #answered.summary()
    #print(answered_list.show())
    for element in answered_list:
        #it will show going packet
        print(element[0].show())
        #it will show receiving packet
        print(element[1].show())
    #     #print(element)
    #     print("------------------")

scan("192.168.0.1/24")
