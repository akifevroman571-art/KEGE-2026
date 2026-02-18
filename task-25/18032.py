def is_prime(num):
    if num == 0:
        return []
    num = abs(n)
    Div = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            Div.append(i)
            if i != n // i:
                Div.append(num // i)
    Div.sort()
    return Div

def f(num):
    d = []
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(i): d += [i]
            if is_prime(num // i): d += sum(map(num))

        if num % 100 == 23:
            return max(d)
    return 0

cnt = 0
for s in range(1000, 10000):
    M = f(s)
    if M:
        print(s, M)
        cnt += 1
        if cnt == 5:
            break