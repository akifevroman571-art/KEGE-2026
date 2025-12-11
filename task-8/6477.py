from itertools import *
cnt = 0
for val in permutations('ЛЕВИОСА'):
    val = ''.join(val)
    if val[0] not in 'ЕОА' and val[3] not in 'ЛВС':
        cnt +=1
print(cnt)