from string import printable as alph
def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]
a = 283**382 + 9**15 + 2**3
b = convert(a, 14).count('b')
c = convert(a, 14).count('c')
print(abs(b - c))
