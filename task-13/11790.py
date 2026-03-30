from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    a = ip[:16].count('0')
    return

ans = []

for a in range(255):
    net = ip_network(f'152.65.245.132/255.255.{a}.0', 0)
    if all(f(i) for i in net):
        print(a)
        break
