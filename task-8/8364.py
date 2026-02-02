from itertools import *
a = sorted('КРАТЕ')
pos1 = 0
pos2=0
for pos, val in enumerate(product(a, repeat=6), start=1):
    val = ''.join(val)
    if val == 'РАКЕТА':
        print(pos)
    if val == 'КАРЕТА':
        print(pos)
a = 9671-6671
print(a-1)