from itertools import *
a = sorted('СТРОКА')

for pos, val in enumerate(product(a, repeat=5)):
    val = ''.join(val)
    if val[0] != 'А' and val[0] != 'Л' and val.count('С') == 1:
        print(pos)
