def f(x, y):
    return (x&a == 0) or not(x & 37 == 0) or not(x & 12 ==0 )

for a in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
