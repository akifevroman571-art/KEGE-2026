from itertools import *
from string import printable
cnt = 0
for val in product(printable[:16], repeat=5):
    val=''.join(val)
    if val.count('6') == 2 and val[0] != '0':
        val = val.replace('6', '.')
        for i in printable[:16:2]:
            val = val.replace(i, '*')
        if '.*' not in val and '*.' not in val and '..' not in val:
            cnt+=1
print(cnt)

