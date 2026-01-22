from itertools import *

a = 'ТИХОРЕЦК'
for val in product(a, repeat=4):
    val = ''.join(val)
    if len(set(val)) == 4:
        for i in 'ИОЕ':
            if i in val:
                glas+=1
            if glas == 2:


