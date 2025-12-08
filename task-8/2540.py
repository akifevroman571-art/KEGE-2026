from itertools import *
a = sorted('АВТОР')
for pos, val in enumerate(product(a, repeat=4), start=1):
    val=''.join(val)
    if val == 'ВАТА':
        print(pos)
