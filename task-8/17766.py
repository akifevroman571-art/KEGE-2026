from itertools import *
a = sorted('СЕНТЯБРЬ')
for pos, val in enumerate(product(a, repeat=5), start=1):
    val=''.join(val)
    if pos % 2 == 0 and val[0] == 'Р' and val.count('Ь') == 0:
        print(pos)