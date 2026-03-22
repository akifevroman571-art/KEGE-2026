def f(x):
    res=''
    while num:
        res+=str(x%5)
        x//=5
    return res
for n in range(1, 10000):
    r = f(n)
    if sum(map(int, r)) % 5 == 0:
        r = r.translate(str.maketrans("10", "01"))+'14'
    else:
        r = r + '33'
