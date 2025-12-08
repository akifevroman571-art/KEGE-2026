cnt = 0
from itertools import *
a = 'БЕРСК'
for i in range(5, 8):
    for pos, val in enumerate(product(a, repeat=i)):
        val=''.join(val)
        cnt+=1
print(cnt)