from itertools import *
a = sorted('ГОНДУБШ')
for pos, val in enumerate(product(a, repeat=6), start=1):
    val=''.join(val)
    if val[0] not in 'Б' and val.count('Н') >= 2 and val.count('У') == 0 :
        print(pos)