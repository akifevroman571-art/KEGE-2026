cnt = 0
cnt1 = 0
from itertools import *
a = sorted('НОРМАЛЬЕ')
for pos, val in enumerate(product(a, repeat=6),start=1):
    val = ''.join(val)
    if val[0] == 'НОРМ':
        print(pos, val)
