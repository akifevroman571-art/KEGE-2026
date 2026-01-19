def f(x, y):
    return (y + 4 * x != 78125) or (a > x) and (a > y)
for a in range(1, 100000):
    if all(f(x, y) for x in range(1,100000) for y in range(1, 100000)):
        print(a)
        break