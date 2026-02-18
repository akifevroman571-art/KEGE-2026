from itertools import *
from string import printable
cnt =0
for val in product(printable[:10], repeat=4):
    val = ''.join(val)
    if len(set(val)) == len(val) and val[0] != '0':
        for i in printable[:10:2]:
            val = val.replace(i, '*')
        for i in printable[1:10:2]:
            val = val.replace(i, '+')
        if '**' not in val and '++' not in val:
            cnt += 1
print(cnt)
