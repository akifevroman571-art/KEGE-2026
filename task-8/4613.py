from itertools import *
from string import printable
cnt = 0
for val in product(printable[:9], repeat=5):
    val=''.join(val)
    if val[-1] != '1' and val[-1] != '8' and val.count('3') <= 1 and val[0] != '0':
        for i in printable[1:9:2]:
            val = val.replace(i, '+')
        if val[0] != '+':
            cnt+=1
print(cnt)