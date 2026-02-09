from string import printable
from itertools import *
cnt = 0
for val in product(printable[:8], repeat=5):
    if val[0] != '0' and val.count('1') == 1:
        for i in '0246':
            val = val.replace(i, '*')
        for i in '1357':
            val = val.replace(i, '+')
        if '**' not in val and '++' not in val:
            cnt+=1
print(cnt)
