from itertools import *
alph = sorted('СТРОКА')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val=''.join(val)
    if val[-1] not in 'АЛ' and val.count('С') ==1:
        if pos % 2 != 0:
            print(pos)

