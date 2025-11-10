# Система счисления
# двоичная система
N = 25
print(bin(N)[2:])
print(f'{N:b}')

# Восьмеричная система
print(oct(N)[2:])
print(f'{N:0}')


# Шестнадцатеричная система
print(hex(N)[2:])
print(f'{N:x}')

# Перевод в любую систему(2 <= sys <=9)
def convert(num, sys):
    res = ''
    while num:
        res += str( num % sys)
        num //= 3
    return res[::-1]


# Перевод в любую систему(2 <= sys <=36)

from string import printable as pp
def convert(num, sys):
    res = ''
    alph = pp
    while num:
        res += alph[num % sys]
        num //= 3
    return res[::-1]

# Перевод в 10-ую систему счисления
bin_num = '101'
oct_num = '765'
tri_num = '1201'
print(int(bin_num), 2)
print(int(oct_num), 8)
print(int(tri_num), 3)

# Сумма цифр числа
# двоичное число
R_1 = '101'
sum_1 =R_1.count('1')

# Число в любой системе до м10 включительно
R_3 = 'AF7'
sum_3 = sum(map(lambda x: int(x , 36), R_3))




