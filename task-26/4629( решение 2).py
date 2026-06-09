with open(r'files/26_4629.txt') as f:
    N = int(f.readline())
    tovar = [int(i) for i in f]
tovar = sorted(tovar)

sale = N // 4

check_2 = sum(tovar) - sum(tovar[:sale]) // 2
print(check_2)

check_1 = sum(tovar) - sum(tovar[-sale:]) // 2
print(check_1)