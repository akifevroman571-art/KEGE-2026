from string import printable as alp
def f(n, s):
    res=''
    while n:
        res+=alp[n%s]
        n//=s
    return res[::-1]


for x in range(1, 9431):
    a = f(39 ** 483 + 39 * 235 - x, 39)
    print(a.count('0'))






