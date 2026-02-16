ans = []
from itertools import *
a = sorted("СДАЙЕГЭ")
for pos, val in enumerate(product(a, repeat=6)):
    val=''.join(val)
    if 'ЕГЭ' in val:
        ans.append(pos)
print(sum(ans))