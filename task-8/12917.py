from itertools import *
a = 'ПРОСТО'
cnt = 0
for val in set(permutations(a)):
    if 'ОО' not in ''.join(val):
        cnt+=1
print(cnt)
