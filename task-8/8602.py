from itertools import *
a = 'АЕНКС'
for pos, val in enumerate(permutations(a), start=1):
    val =''.join(val)
    if 'СЕНЕКА' in val:
        print(pos)