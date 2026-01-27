def f(a):
    for x in range (0, 1000):
        for y in range(0, 1000):
            f = (x*y >a) or (x >y) or (11 > x)
            if not f:
                return False
    return True
for a in range(1, 1000):
    if f(a):
        print(a)