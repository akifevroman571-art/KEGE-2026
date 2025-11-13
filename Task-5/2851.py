for N in range(1, 10000000):
    R = f'{N:b}'
    p_1 = R[1::2].count('1')
    p_2 = R[::2].count('0')
    res = abs(p_1 - p_2)
    if res == 5:
        print(N)
        break
