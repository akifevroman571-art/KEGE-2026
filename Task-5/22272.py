ans =[]
from string import printable as alph
def x (num, sys):
    res = ''
    while num:
        res+= alph[num % sys]
        num //=sys
    return res[::-1]
for n in range(1, 100000):
    R = x(n, 9)
    if R[-1] == 7:
        R = R.replace('6', '*').replace('3', '6').replace('*', '3').replace('*', '3')+ '34'
    else:
        R = '3' + R[1:] + '45'
    R = int(R, 9)
    if R < 2876:
        ans.append([R, n])
print(max(ans))