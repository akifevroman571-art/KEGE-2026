def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []

for n in range(1, 1000000):
    R = convert(n, 3)
    if n % 3 == 0:
        R = R + R[-2:]
    else:
        R = R + convert(sum(map(int, R)), 2)
    R = int(R, 3)
    if R > 220:
        ans.append(R)
print(min(ans))
