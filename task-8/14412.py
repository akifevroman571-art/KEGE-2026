from itertools import *
cnt  = 0
a = 'АЛГОРИТМ'
for val in product(a, repeat=6):
    val=''.join(val)
    if val.count('Л') <= 1 and val[0] != 'Р' and val[-1] not in 'ЛГРТМ':
        cnt+=1
print(cnt)
