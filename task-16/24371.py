from functools import lru_cache


@lru_cache(None)
def f(n):
    return g(n-2)
@lru_cache(None)
def g(n):
    if n < 100: return n
    return f(n-3) + 1
for i in range(1, 5000):
    g(i)
print(f(5000))
