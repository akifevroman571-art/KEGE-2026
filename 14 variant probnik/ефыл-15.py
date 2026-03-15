def f(x, y):
    return (43158 != 3*y+5*x) or (A>x) or (A>y)

for A in range(1, 100000):
    if all(f(x, y) for x in range(1, 100000) for y in range(1, 100000)):
        print(A)
        break

