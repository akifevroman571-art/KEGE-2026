with open(r'files/26_4660.txt') as f:
    N = int(f.readline())
    tovar = [int(i) for i in f]
tovar = sorted(tovar)

sale = N // 4

# 2 ответ
check_2 = sum(tovar) - sum(tovar[:sale]) // 2
print(check_2)


mnogo_cheks = sum(tovar) - sum(tovar[::-1][3::4]) // 2
print(mnogo_cheks)
