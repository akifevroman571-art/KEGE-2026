from itertools import *
from string import printable
cnt = 0
for val in product(printable[:20], repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        for i in printable[:20:2]:
             val = val.replace(i, '*')
        for i in printable[1:20:2]:
            val = val.replace(i, '+')
        if '*+*+*' in val and '+*+*+' in val and val[0] + val[1] == '26':
            cnt +=1
print(cnt)
