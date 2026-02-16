ans = []
def f(num, sys):
    res = ''
    while num:
        res += str( num % sys)
        num //= 3
    return res[::-1] if res else '0'
for n in range(1, 100000):
    r = f(n, 3)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r = r + f(n % 3*4, 3)
    r = int(r, 3)
    if r < 100:
        ans.append(n)
print(max(ans))


