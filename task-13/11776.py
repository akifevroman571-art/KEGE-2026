from ipaddress import *
ans = []

cnt = 0
net = ip_network(f'235.86.56.0/255.255.248.0', 0)
for ip in net:
    ip = f'{int(ip):032b}'
    print(ip)
    if ip[-2:] == '11':
        cnt+=1
print(cnt)