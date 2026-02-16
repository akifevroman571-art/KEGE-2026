from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 6:
        return n
    return (3*n-2)*f(n-5)
for n in range(0, 20569):
    f(n)
print((f(20568) - 51702*f(20563)) // f(20553))
