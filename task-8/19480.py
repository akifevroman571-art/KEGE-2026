from itertools import *
cnt = 0
a = 'ПАРИЖАНКА'
for val in set(permutations(a)):
    val=''.join(val)
    f = 0
    for i in range(len(val)-1):
        if val[i] in 'АИ' and  val[i+1] in 'АИ':
            f+=1
    if f == 1:
        cnt+=1
print(cnt)