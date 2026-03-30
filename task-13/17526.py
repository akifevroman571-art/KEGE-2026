from ipaddress import *
cnt=0
net = ip_network('172.16.128.0/255.255.192.0')

for i in net:
    i = f'{int(i):b}'
    if i.count('1') % 2 != 0:
        cnt+=1
print(cnt)
