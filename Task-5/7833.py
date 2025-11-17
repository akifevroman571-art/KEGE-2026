ans = []
def convert(num, sys):
    res = ''
    while num:
        res += str( num % sys)
        num //= sys
    return res[::-1]
for n in range(10, 100000):
    R = convert(n, 3)
    if n % 2 == 0:
        R = R + R[-2:]
    else:
        R = R + convert(sum(map(int, R)), 3)
    R = int(R, 3)
    if n > 9:
        ans.append((R, n))

print(min(ans))


