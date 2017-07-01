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

import socket
from platform import system
system_type=system().lower()
version_number="0.0.2"
print("Welcome to Tint server "+version_number+" (pre-alpha) on "+system_type+". Read the docs, dumbo.")

# start listening on port 51674

print("listening on port 51674")
receive=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
receive.bind(('',51674))
receive.listen(5)
input=raw_input("tint-server >>> ")
while True:
	(clientsocket,address)=receive.accept()
	ct=client_thread(clientsocket)
	ct.run()
	if input=="x":
		exit()
	else:
		pass
