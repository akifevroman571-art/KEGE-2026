from string import printable as alph
def f(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]
ans = []
for n in range(1, 10000):
    r = f'{n:b}'
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r = r + f(sum(map(int, r)), 2)
    r = int(r, 2)
    if r > 150:
        ans.append(r)
print(ans)