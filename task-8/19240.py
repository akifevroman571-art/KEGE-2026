from itertools import *
a = sorted('ЯНВАРЬ')
for pos, val in enumerate(product(a, repeat=5), start=1):
    val=''.join(val)
    if val[0] != 'Я' and val.count('Ь') <= 1 and 'ЯЯ' not in val:
        print(pos)