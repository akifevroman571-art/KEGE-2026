for n in range(1, 10000):
    r = f'{n:b}'
    if r.count('1') % 2 == 0:
        r = '10' + r[2:] + '1'
    else:
        r = '11' + r[2:] + '0'
    r = int(r,2)
    if n < 16:
        print(r)