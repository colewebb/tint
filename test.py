from platform import system
from subprocess import call
def ping(host):
	parameters = "-n 1" if system().lower()=="windows" else "-c 1 -W 3"
	return call("ping "+parameters+" "+host, shell=True) == 0
i=0
hosts=[]
while i<=264:
	if ping("192.168.0."+str(i))==True:
		hosts.append("192.168.0."+str(i))
	i=i+1
print([hosts])
