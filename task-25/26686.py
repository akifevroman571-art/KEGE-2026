def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i < int(num ** .5) + 1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    return d

cnt = 0
for N in range(89_428_304 + 1, 10 ** 10):
    d = fact(N)
    if len(d) >= 6 and N % sum(d) == 0:
        print(N, sum(d))
        cnt += 1
        if cnt == 6:
            break

