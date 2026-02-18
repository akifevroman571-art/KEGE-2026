from itertools import *
a = 'ДЖАВАСКРИПТ'
for val in permutations(a):
    val=''.join(val)
    for i in val:
        if i in 'АИ':
            b = val.index('А')
            c = val.index('И')
            ans = b + c + 1
print(ans)


