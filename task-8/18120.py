from itertools import *
cnt = 0
sogl =0
a = sorted('ПРЕСТОЛ')
for pos, val in enumerate(product(a, repeat=5), start=1):
    val=''.join(val)
    if pos % 2 == 1 and val[-1] == 'О' and val[-1] == 'Е':
        for i in val:
            if val == 'П' and val == 'Р' and val == 'C' and val == 'Т':
                sogl +=1
        if sogl <= 3:
           cnt +=1
print(cnt)