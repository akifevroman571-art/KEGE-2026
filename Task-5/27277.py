def f(n):
    res = ''
    while n:
        res += str(n%3)
        n//=3
    return res[::-1]
ans = []
for n in range(1, 10000):
    r = f(n)
    if n % 3 != 0:
        r = '1' + r + r[-3:]
    else:
        r = f(sum(map(int, r))*8)
    r = int(r, 3)
    if 1200 <= r <= 1230:
        ans.append(r)
print(max(ans))

