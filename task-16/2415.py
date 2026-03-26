from sys import setrecursionlimit

def f(n):
    if n <= 5: return 1
    return n+f(n-2)

steps_amount = 2000
setrecursionlimit(steps_amount)
print(f(2126)-f(2122))