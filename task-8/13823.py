from itertools import *

a = sorted('МИЗАНТРОП')

for pos, val in enumerate(product(a, repeat=5), start=1):
    val =''.join(val)
    if pos % 2 == 0 and val[0] == 'Н' and val.count('Р') == 2:
        print(pos)