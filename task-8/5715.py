cnt = []
from itertools import *
a = 'ПКБ'
for i in range(1, 16):
    for val in product(a, repeat=i):
        val=''.join(val)
        if val.count('К') > val.count('П') > val.count('Б'):
            C = [val.count('К'), val.count('П'), val.count('Б')]
            if C not in cnt:
                cnt.append(C)
print(len(cnt))
