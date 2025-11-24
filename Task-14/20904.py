def con(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]




for x in range(1, 2031)[::-1]:
    a = con(3**100 - x, 3)
    if a.count('0') == 1:
        print(x)
        break

