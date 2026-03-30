from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return ip[:16].count('0') <= ip[16:].count('0')

ans = []

for a in range(256)[::-1]:
    net = ip_network(f'223.167.{a}.167/255.255.255.192', 0)
    if all(f(i) for i in net):
        print(a)
        break
