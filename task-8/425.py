from itertools import *
cnt = 0
for val in permutations('ЗАПИСЬ'):
    val=''.join(val)
    if val[0] != 'Ь' and 'ИЬ' not in val and 'АЬ' not in val:
        cnt+=1
print(cnt)