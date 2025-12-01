
cnt1 = 0
cnt2 = 0

from string import printable as alph
def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]
num = convert((15*343**2031 + 7*49**1142 - 3*7**111 + 7**222 - 16809), 7)

for i in range(len(num)):
    if int(num[i]) % 2 == 0:
        cnt1+=1
    else:
        cnt2+= 1
print(cnt1 - cnt2)

