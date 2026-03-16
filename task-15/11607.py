def D(n, m):
    return n % m == 0

def f(x):
    return not (D(x, 263) <= D(x, A)) and D(x, 71)
for A in range(1, 20000)[::-1]:
    if all(not f(x) for x in range(1, 20000)):
        print(A)
        break
