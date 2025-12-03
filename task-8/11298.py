cnt = 0
from itertools import *
alph = sorted('АОЖПЮЗ')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] in 'А' and val.count('З') >=2:
        if pos % 2 == 0:
            cnt+=1
print(cnt)