from itertools import *
a = sorted('АБИКОЛУН')
for val in product(a, repeat=8):
    val=''.join(val)
