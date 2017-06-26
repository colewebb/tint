import socket
from subprocess import Popen
p=Popen("ping -c 2 scanme.nmap.org",shell=True)
print(p)
