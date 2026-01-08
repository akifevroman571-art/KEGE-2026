ans =[]
def f(num, sys):
    res = ''
    while num:
        res += str( num % sys)
        num //= sys
    return res[::-1]
for n in range(1, 100000):
    r = f(n, 3)
    if sum(map(int, r)) % 2 == 0:
        r = '1' + r +'2'
    else:
        r = '2' + r + '0'
    r = int(r,3)
    if r > 100:
        ans.append(r)
print(min(ans))

