def f(n, s):
    res=''
    while n:
        res+=str(n%s)
        n//=s
    return res
ans = []
for n in range(1, 10000):
    r = f'{n:b}'
    if n % 3 == 0:
        r = r + r[:-3]
    else:
        r = r + f((n%3*3), 2)
    r = int(r,2)
    #if r > 130:
    if r < 130:
        ans.append([r, n])
print(ans)
