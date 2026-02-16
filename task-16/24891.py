from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 10:
        return n
    return n-7 +f(n-21)
for n in range(0, 185735):
    f(n)
print((f(185734)-f(185650))//f(40))
