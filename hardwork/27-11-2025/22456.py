for n in range(1,100000):
    R = f'{n:b}'
    if  R.count('1') % 2 == 0:
        R = '11' + R[2:] + '1'
    else:
        R = R + '0'
        if R.count('0')<R.count('1'):
            R = R + '1'
    R = int(R, 2)
    if R > 271:
        print(n)
        break

