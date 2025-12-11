from itertools import *
a = '0123456789ABCDEF'
cnt = 0
for val in product(a, repeat=4):
    val = ''.join(val)
    if val.count('3') == 1 and val[-1] != '0':
        for i in range(3):
            if val[i] == val[i+1]:
                break
        else:
            cnt +=1
print(cnt)