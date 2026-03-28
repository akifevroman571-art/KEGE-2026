with open(r'../task-26/files/26_4684.txt') as file:
    N = int(file.readline())
    tovar = [int(i) for i in file]

tovar = sorted(tovar)
sale = N// 6
one_check   = sum(tovar) - sum(tovar[:sale]) // 2
may_checks = sum(tovar) - sum(tovar[::-1][5::6]) // 2

print(may_checks, one_check)
