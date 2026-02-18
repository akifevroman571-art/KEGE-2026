def is_prime(n):
    if n == 0:
        return []
    n = abs(n)
    Div = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            Div.append(i)
            if i != n // i:
                Div.append(n // i)
    Div.sort()
    return Div

def f(num):

    d = []
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(i): d += [i]
            if is_prime(num // i): d += [num // i]
    if sum(is_prime(i)) // len(is_prime(i)):
        if num % 100 == 12:
            return
    return 0

cnt = 0
for s in range(700000, 10**20):
    M = f(s)
    if M:
        print(s, M)
        cnt += 1
        if cnt == 5:
            break
