cnt = 0
from itertools import *
a = sorted('АПРЕЛЬ')[::-1]
for pos, val in enumerate(product(a, repeat=5)):
    if val[-1] == 'Ь':
        if pos <= 387:
            cnt+=1
print(cnt)