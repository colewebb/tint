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

# imports, startup message

# imports

import socket
from platform import system
from subprocess import call
from uuid import getnode
from os import path

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

# start listening on port 51674

print("listening on port 51674")
receive=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
receive.bind(('',51674))
receive.listen(5)
while True:
	(client_socket,client_address)=receive.accept()
	request=client_socket.recv(1024)
	print request
	recieve.close()
	
