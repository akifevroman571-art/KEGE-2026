def f(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i * i <= num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    return d
cnt = 0
for i in range(3_600_001, 10**8):
    m = f(i)
    if len(m) == 3 and all('3' in str(M) and '5' in str(M) for M in m):
            print(i, m[-1])
            cnt +=1
            if cnt == 5:
                break



