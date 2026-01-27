def f(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res[::-1] else '0'
ans = []
for n in range(0, 100000):
    r = f(n, 4)
    if n % 2 == 0:
        r = '12' + r + f(int(r[-1]) * 3, 4)
    else:
        r = '21' + r + '13'
    r = int(r, 4)
    if r > 50:
        ans.append(r)
print(min(ans))