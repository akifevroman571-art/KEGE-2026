for N in range(1, 1000000):
    R = f'{N:b}'
    if R.count('1') % 2 == 0:
        R += '10'
    else:
        R = '1' + R[2:] + '01'
    if R >= 30:
        print(N)
        break