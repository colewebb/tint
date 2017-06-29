# Tint: file sharing made much simpler
# 
#    This file is part of Tint.
#
#    Copyright (C) 2017 Cole Webb
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

# imports

import socket
from platform import system
from subprocess import call, Popen
from uuid import getnode

# getting system type

system_type=system().lower()
version_number="0.0.1"

# printing welcome, license info

print("Welcome to Tint "+version_number+" on "+system_type+". Read the docs, dumbo.\n\nTint Copyright (C) 2017 Cole Webb\nThis program comes with ABSOLUTELY NO WARRANTY. This is free software, and\nyou are welcome to redistribute it under certain conditions. See the file\nlicense for more information on warranty restrictions and redistribution.\n")

# getting local ip address

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("10.255.255.255", 80))
	ip_address=s.getsockname()[0]
	s.close()
	print(ip_address)
except:
	print("Using this program requires a network connection, and one was not found.\nNow exiting...")
	exit()

# getting mac address

mac_address=getnode()
# print(':'.join(("%012X" % mac_address)[i:i+2] for i in range(0, 12, 2)))
if (mac_address >> 40)%2:
	print("No valid MAC address was found. Exiting...")
	exit()

# function definitions

def find_peers():
	print("Using nmap to find potential peers on the network, please wait...")
	call("nmap -p 51674 192.168.0.0/24 | grep 'Nmap scan report' > /home/rebooted/scripts/tint/hosts.txt",shell=True)
	print("nmap host discovery completed. moving on to connection testing...")
	peers=open("/home/rebooted/scripts/tint/hosts.txt")
	potential_peer_list=[]
	peer_list=[]
	for line in peers:
		potential_peer_list.append(line[21:].rstrip())
	for peer in potential_peer_list:
		try:
			send.connect((peer,51674))
			send.send("tint "+version_number+" "+system_type+" "+ip_address+" "+mac_address)
			peer_found=True
		except:
			peer_found=False
		if peer_found==True:
			peer_list.append(peer)
			print("Peer found on "+peer+".")
		else:
			print("Peer not found on "+peer+".")
	return peer_list

# setup client socket

send=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
send.settimeout(5)

command=raw_input("tint >>> ")
while True:
	if command=="x":
		exit()
	elif command=="exit":
		exit()
	elif command=="scan":
		peers=find_peers()
		print(peers)
	else:
		print("Command '"+command+"' is not found. Try:\n\n - scan: scan network for peers\n - send: send a file to a peer\n - exit: exit the program\n")
	command=raw_input("tint >>> ")
# return list of ip and mac addresses, and aliases from configuration file (if available)

# offer prompt
# options:
#	- list: print list of available devices
#	- send: send file
#	- exit: shutdown correctly

# list: return list of ip and mac addresses, and aliases from configuration file (if available)

# send: use tint protocol to send file, including encryption key exchange, file information, confirmation, etc.

# exit: notify other computers of exit, save files, exit

send.close()
