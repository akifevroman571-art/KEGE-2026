from itertools import *
cnt = 0
a = 'КИДАЛА'
for val in set(permutations(a, r=5)):
    val = ''.join(val)
    if 'АА' not in val:
        cnt +=1
print(cnt)