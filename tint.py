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
from subprocess import call
from uuid import getnode
from os import path
from time import sleep

# getting system type

system_type=system().lower()

# getting installation location

file_location=path.realpath(__file__)
install_location=file_location[:-7]

# printing welcome, license info

version_number="0.0.2"
print("Welcome to Tint "+version_number+" on "+system_type+". Read the docs, dumbo.\n\nTint Copyright (C) 2017 Cole Webb\nThis program comes with ABSOLUTELY NO WARRANTY. This is free software, and\nyou are welcome to redistribute it under certain conditions. See the file\nlicense for more information on warranty restrictions and redistribution.\n")

# getting local ip address

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("10.255.255.255", 80))
	ip_address=s.getsockname()[0]
	s.close()
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
	execute_line=install_location+"nmap -p 51674 192.168.0.0/24 | grep 'Nmap scan report' > "+install_location+"hosts.txt"
	call(execute_line,shell=True)
	print("nmap host discovery completed. moving on to connection testing...")
	peers=open(install_location+"hosts.txt")
	potential_peer_list=[]
	peer_list=[]
	for line in peers:
		potential_peer_list.append(line[21:].rstrip())
	for peer in potential_peer_list:
		print peer
		send=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		try:
			send.connect((str(peer),51674))
			send.send("tint")
#			send.send("tint "+version_number+" "+system_type+" "+ip_address+" "+mac_address)
#			sleep(0.01)
			peer_found=True
			send.close()
		except:
			print("Host not found on "+peer+".")
		if peer_found==True:
			peer_list.append(peer)
			print("Peer found on "+peer+".")
		else:
			print("Peer not found on "+peer+".")
	return peer_list

def correct_shutdown():
	exit()

def transfer():
	file_location=raw_input("Please input the path of the file you would like to send: ")
	try:
		transfer_file=open(file_location)
		print("file found")
		transfer_file.close()
		pass
	except:
		print("That doesn't appear to be a valid file path. Check the path and try again.")
		pass

# set up input loop

while True:
	command=raw_input("tint >>> ")
	if command=="x":
		correct_shutdown()
	elif command=="exit":
		correct_shutdown()
	elif command=="scan":
		peers=find_peers()
	elif command=="send":
		transfer()
	else:
		print("Command '"+command+"' is not found. Try:\n\n - scan: scan network for peers\n - send: send a file to a peer\n - exit: exit the program\n")

# return list of ip and mac addresses, and aliases from configuration file (if available)

# offer prompt
# options:
#	- list: print list of available devices
#	- send: send file
#	- exit: shutdown correctly

# list: return list of ip and mac addresses, and aliases from configuration file (if available)

# send: use tint protocol to send file, including encryption key exchange, file information, confirmation, etc.

# exit: save files, exit

correct_shutdown()
