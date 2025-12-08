cnt = 0
from itertools import *
a = ('ПОЛИНА')
for val in product("ПОЛИНА", repeat=8):
    val = ''.join(val)
    sogl = val.count('О') + val.count('И') + val.count('А')
    glas = val.count('П') + val.count('Л') + val.count('Н')
    if sogl > glas:
        cnt+=1
print(cnt)
