from math import prod
def f(num):
    d = set()
    for i in range(1, int(num**.5)+1):
        if num % i == 0:
            d |= {num // i, i}
    if len(d) > 10:
        if prod(d) % 2 != 0:
            if sum(d) % 2 != 0:
                return len(d)
    return 0
cnt = 0
for n in range(800001, 10**8):
    m = f(n)
    if m:
        print(n, m)
        cnt+=1
        if cnt ==6:
            break







