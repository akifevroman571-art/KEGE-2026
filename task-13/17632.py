from ipaddress import *
cnt=0
net = ip_network('112.160.0.0/255.240.0.0', False)

for i in net:
    i = f'{int(i):b}'
    if i.count('1') % 5 == 0:
        cnt+=1
print(cnt)