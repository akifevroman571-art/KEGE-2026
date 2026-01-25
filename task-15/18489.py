def c(x, y):
    return x % 10 == y % 10

def f(x):
    return ((x % 10 != 5) and c(x, 4)) <= (x > a - 11)
for a in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break
