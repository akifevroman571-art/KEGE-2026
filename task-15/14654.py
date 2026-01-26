def d(n, m):
    return n % m == 0
def f(x):
    return d(x, A) or (d(x, 133) <= (not d(x, 95)))
for A in range(1, 10000)[::-1]:
    if all(f(x) for x in range(1, 10000)):
        print(A)
        break

