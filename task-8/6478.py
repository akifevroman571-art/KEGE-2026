from itertools import *
cnt = 0
a = 'МОЛЬ'
for val in product(a, repeat=5):
    val=''.join(val)
    if val[0] != 'Ь' and 'ЬЬ' not in val and 'ОЬ' not in val:
        cnt+=1
print(cnt)
