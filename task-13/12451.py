from ipaddress import ip_network, ip_address


def f(ip):
    ip = f'{int(ip):032b}'
    return ip[16:24].count('0') > ip[24:].count('0')

cnt = 0
for A in range(256):
    ip_host = ip_address(f'246.81.65.{A}')
    net = ip_network(f'{ip_host}/27', False)
    if ip_host in net.hosts() and all(f(host) for host in net.hosts()):
        cnt += 1

print(cnt)