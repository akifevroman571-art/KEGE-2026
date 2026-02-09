from string import printable as alph
def f(n, s):
    res = ''
    while n:
        res +=alph[n % s]
        n//=s
    return res[::-1]
ans = []
for n in range(1, 1000):
    R = f(n, 7)
    if R[-1] == '0':
        R = '33' + R.replace('1', '*').replace('3', '1').replace('*', '3')
    else:
        R = '1' + R[1:] + '36'
    R = int(R, 7)
    if R < 744:
        ans.append([R, n])
print(sorted(ans, key=lambda x:[-x[0], x[1]]))
