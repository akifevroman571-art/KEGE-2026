cnt = 0
from itertools import *
a = ('ГЕПАРД')
for val in product(a, repeat=5):
    val=''.join(val)
    if val.count('Г') == 1 and val[0] != 'А' and val[-1] != 'Е':
        cnt+=1
print(cnt)