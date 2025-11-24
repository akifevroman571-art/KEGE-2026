def con (num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
for x in range(1, 3001):
    a = con(9**150 + 9**30 - x, 9)
    if a.count('0') == 122:
        print(x)
        break

