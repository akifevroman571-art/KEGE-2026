from ipaddress import *

ip_1 = ip_address('201.44.240.33')
ip_2 = ip_address('201.44.240.107')
cnt = 0
for i in range(10, 31):
    net1 = ip_network(f'{ip_1}/{i}', False)

    if ip_1 in net1.hosts() and ip_2 in net1.hosts():
        a = f'{int(net1.network_address):032b}'
        if a.count('1') >=5:
            cnt+=1


print(cnt)