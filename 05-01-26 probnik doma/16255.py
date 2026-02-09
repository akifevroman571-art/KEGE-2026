
from itertools import product
from string import printable
cnt = 0
for val in product(printable[:9], repeat=7):
    val=''.join(val)
    if val[0] not in (0,1,3,5,7) and val[-1] % 3 != 0 and val.count(6) > 0:
        cnt+=1
print(cnt)

def f(t):
    if len(t) == 1 and t[0] in (0, 1, 3, 5, 7):
      return 0
    if len(t) == 7:
      return t[-1] % 3 != 0 and t.count(6) > 0
    return sum(f(t+[x]) for x in range(9))

print(f([]))