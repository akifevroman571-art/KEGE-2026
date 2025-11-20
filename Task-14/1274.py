def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
a = 729**8 - 3**18 + 85
print(convert(a , 9).count('0'))
