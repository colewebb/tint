# startup, imports

import socket
from os import getenv
from subprocess import call
print("Welcome to Tint 0.0.1 (pre-alpha). Read the docs, dumbo.")

# start listening on port 51674
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.bind((socket.gethostname(),51674))

# scan network for that port on other devices

# return list of ip and mac addresses, and aliases from configuration file (if available)

# offer prompt
# options:
#	- list: print list of available devices
#	- send: send file
#	- exit: shutdown correctly

# list: return list of ip and mac addresses, and aliases from configuration file (if available)

# send: use tint protocol to send file, including encryption key exchange, file information, confirmation, etc.

# exit: notify other computers of exit, save files, exit
