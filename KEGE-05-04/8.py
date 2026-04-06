from string import printable
from itertools import *
cnt = 0
for val in permutations(printable[:7]):
    val = ''.join(val)

    if val[0] != '0' and val[0] != '3' and val[0] !='5' and '22' not in val and '44' not in val:

        print(val)

        cnt+=1
print(cnt)
