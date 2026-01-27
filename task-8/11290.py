from itertools import *
from string import printable
cnt=0
for val in product(printable[:16], repeat=4):
    if val[0] != '0' and val.count('9') == 1:
        for i in '02468101214':
            val=val.replace(i, "*")
        for i in val '1357111315':
            val=val.replace(i, '+')
    if '++' not in val and '**' not in val:
        cnt+=1
print(cnt)
