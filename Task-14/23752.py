from string import printable as alph
def con(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]
cnt = 0
num = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
for i in con(num, 27):
    if int(i, 27) > 9:
        cnt +=1
print(cnt)



