from itertools import *
cnt = 0
for val in set(permutations('РОСОМАХА')):
    val=''.join(['*' if i in 'АО'  else '+' for i in val])
    if '**' not in val and '++' not in val:
        cnt+=1
print(cnt)
