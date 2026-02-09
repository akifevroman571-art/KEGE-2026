def f(a):
    for x in range (0, 1000):
        for y in range(0, 1000):
            f = (x%128==0) or (not(x%a==0)) or (not(x%80==0))
            if not f:
                return False
    return True
for a in range(1, 1000):
    if f(a):
        print(a)