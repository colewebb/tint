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

# imports, startup message, other startup

import socket
from platform import system
from subprocess import call, Popen
system_type=system().lower()
print("Welcome to Tint 0.0.1 (pre-alpha) on "+system_type+". Read the docs, dumbo.\n\nTint Copyright (C) 2017 Cole Webb\nThis program comes with ABSOLUTELY NO WARRANTY; for details type 'show w'.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions; type 'show c' for details.\n")

#function definitions

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
			print("Peer found at "+peer+".")
			peer_list.append(peer)
		except:
			print("No host found on "+peer+".")
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
	elif command=="show w":
		print("There is no warranty for the program, to the extent permitted by applicable\nlaw. Except when  otherwise stated in writing the copyright holders and/or\nother parties provide the program 'as is' without warranty of any kind, either\nexpressed or implied, including, but not limited to, the implied warranties of\nmerchantability and fitness for a particular purpose. The entire risk as to the\nquality and performance of the program is with you. Should the program prove\ndefective, you assume the cost of all necessary servicing, repair or correction.")
	elif command=="show c":
		
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
