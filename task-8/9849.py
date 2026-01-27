from itertools import *
cnt = 0
a = 'ABCDEF'
for val in product(a, repeat=6):
    val = ''.join(val)
    if val[0] != 'A' and val[0] != 'E' and val[-1] != 'A' and val[-1] != 'E':
        cnt+=1
print(cnt)

