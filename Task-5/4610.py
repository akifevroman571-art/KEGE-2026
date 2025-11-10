for N in range(1, 1000000):
    R = f'{N:b}'
    if sum(map(int, R)) % 2 == 0:
        R = '10' + R[2:] + '0'
    else:
        R = '11' + R[2:] + '1'
    R = int(R, 2)
    if R < 35:
        print(N)


