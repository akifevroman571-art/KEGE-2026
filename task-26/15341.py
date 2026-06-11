with open(r'files/26_15341.txt') as f:
    N = int(f.readline())
    cakes = {int(i) for i in f}

cakes = sorted(cakes, reverse=True)
last_cake = cakes[0]
cnt = 1

for cake in cakes:
    if last_cake - cake >= 8:
        last_cake = cake
        cnt += 1
print(cnt, last_cake)