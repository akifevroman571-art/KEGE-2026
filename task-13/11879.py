from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return ip[:16].count('1') < ip[16:].count('1')

ans = []

for a in range(255):
    net = ip_network(f'99.8.254.232/255.255.{a}.0', 0)
    if all(f(i) for i in net):
        print(a)
        break