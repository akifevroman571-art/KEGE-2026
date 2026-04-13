import ipaddress
from ipaddress import *

ip_1 = ipaddress.ip_address('211.115.61.154')
ip_2 = ipaddress.ip_address('211.115.59.137')

for mask in range(16, 31)[::-1]:
    net = ip_network(f'{ip_1}/{mask}',0)
    if ip_1 in net.hosts() and ip_2 in net.hosts():
        print(net.netmask)
        break