def f(n, m):
     return n % m == 0
def g(x):
    if a != 0:
        return f(a, 25) and ((f(x, 24) and f(x, 75)) <= f(x, a))
ans = []
for a in range(-10000, 10000):
    if all(g(x) for x in range(-10000, 10000)):
        ans.append(a)
print(len(ans))

