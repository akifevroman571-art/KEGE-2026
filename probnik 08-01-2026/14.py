def convert(num, sys):
    res = ''
    while num:
        res += str( num % sys)
        num //= sys
    return res[::-1]
cnt = 0
for x in range(10, 70001):
    a = convert(5 ** 2025 + 5 ** 400 - x, 5)
    for i in a:
        if i.count('4') == 1:
            cnt +=1
print(cnt)




