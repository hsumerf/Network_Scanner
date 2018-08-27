# It will tell the MAC addres of IP address holder
#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan("172.17.0.1/24")