from itertools import *
a = sorted('ПАРУС')
for pos, val in enumerate(product(a, repeat=5),start=1):
    val=''.join(val)
    if val[0] == 'У' and val.count('АА') == 0 and val.count('А') == 2:
        print(pos)