def is_prime(num):
    if num == 0:
        return []
    num = abs(n)
    Div = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            Div.append(i)
            if i != n // i:
                Div.append(num // i)
    Div.sort()
    return Div

def f(num):
    d = []
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0 and is_prime(i):
            d.append(i)
    if n % (n // u) == 0 and p(n // u):
        d.append(n // u)
    return list(set(d))

w = []
for u in range(1000001, 10 ** 20):
l = f(u)
if len(l) == 3:
        w.append((u, max(l)))
    if len(w) == 5:
        break
for u in w:
    print(*u)



