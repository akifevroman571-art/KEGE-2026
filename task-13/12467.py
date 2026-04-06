from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return ip[17:33].count('1') > 3

ans = []

for a in range(255):
    net = ip_network(f'183.192.{a}.0/255.255.252.0', 0)
    if all(f(i) for i in net):
        print(a)
        break