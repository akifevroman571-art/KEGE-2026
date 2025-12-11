from itertools import *
cnt = 0
for val in permutations('0123456789', r=6):
    val =''.join(val)
    if val[0] != '0' and int(val) % 4 ==0:
        val=''.join(['*' if i in '02468' else '+' for i in val])
        if '**' not in val:
            cnt+=1
print(cnt)