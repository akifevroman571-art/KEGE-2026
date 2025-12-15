from string import printable as alph
def f(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]
ans = []
for n in range(1, 10000):
    R = f(n, 3)
    if n % 3 ==0:
        R = R + R[-2:]
    else:
        R = R + f(sum(map(int, R))* 3, 3)
    R = int(R, 3)
    if R > 208 and R % 2 == 1:
        ans.append(R)
print(min(ans))




