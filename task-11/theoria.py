from math import *
# 1855
L = 101
N = 4090+10
i = ceil(log2(N)) # bit
I = ceil(L * i / 8)
print(2048*I/2**10)

# 23749 2026 год
for n in range(1, 10**8):
    L = 2783
    i = ceil(log2(n)) # bit
    I = ceil(L * i / 8)
    if 3845627 * I >=11*2**30:
        print(n)
        break
# 23370
for l in range(1, 10**8):
    N = 10+17
    i = ceil(log2(N)) # bit
    I = ceil(l * i / 8)
    if 7564230 * I > 31*2**20:
        print(l)
        break