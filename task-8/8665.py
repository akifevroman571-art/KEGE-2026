from itertools import *
from string import printable
cnt = 0
for val in product(printable[:12], repeat=7):
    val=''.join(val)
    if val[0] != '0' and val.count('b') ==2:
        for i in printable[:12:2]:
            val = val.replace(i, '*')
        for i in printable[1:12:2]:
            val = val.replace(i, '+')
        if '**' not in val and '++' not in val:
            cnt +=1
print(cnt)




