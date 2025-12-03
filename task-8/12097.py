from itertools import *
a = sorted('ГИРЛЯНДА')
for pos, val in enumerate(product(a, repeat=6), start=1):
    val=''.join(val)
    if val[0] not in 'Я' and val.count('Д') == 3:
        if pos % 2 ==0:
            print(pos)