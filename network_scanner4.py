#!usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
# this line will return 2 lists, answered and unanswered.Timeout will specify time to request
    answered_list = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    print("IP\t\t\tMAC address\n-------------------------")
    clients_list = []

    for element in answered_list:
        client_dict = {"ip":element[1].psrc,"MAC":element[1].hwsrc}
        clients_list.append(client_dict)
    print(clients_list)

# usr ifcongig to get to know MAC address of your PC network card
scan("192.168.0.1/24")
