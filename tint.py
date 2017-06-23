# imports, startup message
import socket
from platform import system
from subprocess import call
system_type=system().lower()
print("Welcome to Tint 0.0.1 (pre-alpha) on "+system_type+". Read the docs, dumbo.")
# start listening on port 51674
receive=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
receive.bind(('',51674))
receive.listen(5)
# setup client socket
send=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
send.settimeout(5)
# scan network for that port on other devices
i=0
while i <=264:
	if system_type == "windows":
		stuff_to_call="ping -n 1 192.168.0."+str(i)
		result=call(stuff_to_call,shell=True)
		print(result)
	else:
		stuff_to_call=call("ping -c 1 192.168.0."+str(i)
		result=call(stuff_to_call,shell=True)
		print(result)
# wait for permission to exit...
raw_input("waiting, press enter to exit...")
# return list of ip and mac addresses, and aliases from configuration file (if available)

# offer prompt
# options:
#	- list: print list of available devices
#	- send: send file
#	- exit: shutdown correctly

# list: return list of ip and mac addresses, and aliases from configuration file (if available)

# send: use tint protocol to send file, including encryption key exchange, file information, confirmation, etc.

# exit: notify other computers of exit, save files, exit
receive.close()
