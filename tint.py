# startup, imports
import socket
from os import getenv
from subprocess import call
print("Welcome to Tint 0.0.1 (pre-alpha). Read the docs, dumbo.")
# start listening on port 51674
connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.bind(('',51674))
connection.listen(5)
# scan network for that port on other devices
i=0
hosts=[]
while i <= 264:
	try:
		connection.connect("192.168.0."+str(i),51674)
		hosts=hosts+["192.168.0."+str(i)]
		print("host found")
	except:
		print("No host found on 192.168.0."+str(i)+", moving on.")
	i=i+1
wait_exit=raw_input("waiting, press enter to exit...")
# return list of ip and mac addresses, and aliases from configuration file (if available)

# offer prompt
# options:
#	- list: print list of available devices
#	- send: send file
#	- exit: shutdown correctly

# list: return list of ip and mac addresses, and aliases from configuration file (if available)

# send: use tint protocol to send file, including encryption key exchange, file information, confirmation, etc.

# exit: notify other computers of exit, save files, exit
