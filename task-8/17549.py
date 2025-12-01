from itertools import *
alph = sorted('ФОКУС')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val.count('Ф') == 0 and  val.count('У') == 2:
        print(pos)


