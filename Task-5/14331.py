def con(num, sys):
    res = ''
    while num:
        res += str( num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1, 100000):
    r = con(n, 3)
    a = sum(map(int, r))
    if a % 3 == 0:
        r = r + '212'
    else:
        r = r + con(a * 2, 3)
    r = int(r, 3)
    if r  > 490:
        ans.append(r)

print(min(ans))


