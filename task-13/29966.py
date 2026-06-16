from ipaddress import *

ip = ip_network('146.180.173.153/255.192.0.0', False).hosts()
print(max(ip))