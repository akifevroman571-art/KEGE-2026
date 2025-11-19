def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
a = 16**820 - 2**761 + 14
print(convert(a, 4).count('0'))
