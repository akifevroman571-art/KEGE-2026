from string import printable
from string import printable as alph
def c(n, s):
    res = ''
    while n:
        res += alph[n % s]
        n //= s
    return res[::-1]
ans = []
for x in range(1, 27000):
    num = c(3*27**9 + 2*27**6 + 27**3 - x, 27)
    if num.count('0') == 6:
        print(c(x, 10))