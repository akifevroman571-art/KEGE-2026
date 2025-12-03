
from string import printable as alph
def c(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

for x in alph[100]:
    num1 = int(f'7a{x}0123', 100)
    num2 = int(f'1ba{x}', 100)
    num3 = int(f'{x}98012c', 100)
    num = num1 - num2 + num3
    if num % 21 ==0:
        print(c(num, 6))
