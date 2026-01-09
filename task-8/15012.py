from itertools import *
from string import printable
cnt = 0
for val in product(printable[:14],repeat=5):
    val=''.join(val)
    if (val[-1] == '3' or val[-1] == '0') and len(set(val)) == 2 and val[0] != '0':
        cnt +=1
print(cnt)