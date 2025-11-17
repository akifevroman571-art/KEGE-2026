def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

a = 4 * 625 ** 9 - 25 ** 15 + 2 * 5 ** 11 - 7
print(convert(a, 5).count('4'))


a = 4 * 625 ** 9 - 25 ** 15 + 2 * 5 ** 11 - 7
cnt_4 = 0

while a:
    if a % 5 == 4:
        cnt_4 += 1
    a //= 5
print(cnt_4)

