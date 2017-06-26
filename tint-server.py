# imports, startup message

import socket
from platform import system
system_type=system().lower()
print("Welcome to Tint server 0.0.1 (pre-alpha) on "+system_type+". Read the docs, dumbo.")

# start listening on port 51674

print("listening on port 51674")
receive=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
receive.bind(('',51674))
receive.listen(5)
