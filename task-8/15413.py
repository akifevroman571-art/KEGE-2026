from string import printable as alph
from itertools import *

cnt = 0
for val in product(alph[:9], repeat=4):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1:
        val = val.split('8')
        if sum(map(int, val[0])) == sum(map(int, val[1])):
            cnt += 1
print(cnt)