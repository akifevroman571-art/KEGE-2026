
a = 51 * 7**12 - 7**3 - 22
ans = 0
while a:
    ans += a % 7
    a //= 7
print(ans)

