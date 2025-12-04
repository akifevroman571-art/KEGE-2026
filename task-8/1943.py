cnt = 0
from itertools import *
for val in product('ЗЕРКАЛО', repeat=6):
    val=''.join(val)
    if 'К' in val and val.count('К') <= 4:
        val = val.replace('К', '')
        if len(val) == len(set(val)):
            cnt +=1
print(cnt)