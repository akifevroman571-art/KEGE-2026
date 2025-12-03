from string import printable as alph
def f(n, s):
    res = ''
    while n:
        res +=alph[n % s]
        n//=s
    return res[::-1]
ans = []
for n in range(1, 10000000):
    R = f(n, 5)
    if R[-1] == 0:
        R = R.replace('1', '4').replace('4', '1')
        R = '33' + R.replace('4', '4')
        R = R + '43'

