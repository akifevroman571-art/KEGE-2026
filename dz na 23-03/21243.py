def f(x):
    res=''
    while x:
        res+=str(x%5)
        x//=5
    return res[::-1]
ans = []
for n in range(1, 10000):
    r = f(n)
    if sum(map(int, r)) % 5 == 0:
        r = r.replace('0', '*').replace('1', '0').replace('*', '1') + '14'
    else:
        r = '44' + r[2:] + '33'
    r = int(r, 5)
    if r > 370:
        ans.append([r, n])
print(min(ans))





