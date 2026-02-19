from itertools import *
a = 'ДЖАВАСКРИПТ'
ans = 0
for val in set(permutations(a)):
    val=''.join(val)
    if