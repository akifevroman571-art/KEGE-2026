def f(a):
    for x in range (1, 1000):
        f = ((x % 2 == 0) <= (x % 3 !=0)) or (x + a >= 80)
        if not f:
            return False
    return True
for a in range(1, 1000):
    if f(a):
        print(a)
        break