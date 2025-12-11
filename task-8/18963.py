from itertools import *
cnt = 0
a = 'КОТБУС'
for val in product(a, repeat=8):
    val = ''.join(val)
    if 'КОТ' in val and val[0] != 'У' and val[0] != 'О':
        cnt += 1
print(cnt)


