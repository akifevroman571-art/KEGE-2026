def f(n,s):
    res=''
    while n:
        res +=str(n%s)
        n//=s
    return res[::-1]
for n in range(1, 10000):
    r = f(n, 4)
    if n %4 == 0:
        r = r+ r[:2]
    else:
        r = r+f(n%4*4, 4)
    r = int(r, 4)
    if r > 291:
        print(r)
        break
