from string import printable as alph
def f(n, s):
    res = ''
    while n:
        res +=alph[n % s]
        n//=s
    return res[::-1]
ans = []
for n in range(1, 1000):
    R = f(n, 5)
    if R[-1] == '0':
        R = '33' + R.replace('1', '*').replace('4', '1').replace('*', '4')
    else:
        R = '3' + R[1:] + '42'
    R = int(R, 5)
    if R < 1922:
        ans.append([R, n])
print(sorted(ans, key=lambda x:[-x[0], x[1]]))




