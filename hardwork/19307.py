cnt = 0
from string import printable as alph
def c(n, s):
    res = ''
    while n:
        res +=alph[n % s]
        n//=s
    return res[::-1]
a = 15625**16 - 3125**3 * 25**19 + 625**4 - 2005
b = c(a, 5)
print(b.count('0'))