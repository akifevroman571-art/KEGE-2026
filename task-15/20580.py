def f(a):
    for x in range (1, 1000):
        for y in range(1, 1000):
            f = (9*x + y > a) or (x >= 36) or (y >= 18)
            if not f:
                return False
    return True
for a in range(1, 1000):
    if f(a):
        print(a)