cnt = 0
from itertools import *
a = 'ПСКАЛЬ'
for val in product(a, repeat=4):
    val=''.join(val)
    if val[0] != 'Ь' and 'ЬЬ' not in val:
        cnt+=1
print(cnt)
