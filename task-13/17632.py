from ipaddress import *
cnt=0
net = ip_network('112ю')

for i in net:
    i = f'{int(i):b}'
    if i.count('1') % 3 != 0:
        cnt+=1
print(cnt)