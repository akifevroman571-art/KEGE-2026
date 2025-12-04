cnt = 0
from itertools import *
a = sorted('СОЛНЦЕ')
for pos, val in enumerate(product(a, repeat=6),start=1):
    val=''.join(val)
    if val[0] not in 'ЕО' and val.count('Ц') == 2:
        if pos % 2 ==0:
            cnt+=1
print(cnt)
