from itertools import *
from string import printable
cnt=0
for val in product(printable[:7], repeat=5):
    val=''.join(val)
    if val[0] != '0' and val[-1] not in '012' and val.count('4') <= 1 and val[0] in '246':
        cnt+=1
print(cnt)