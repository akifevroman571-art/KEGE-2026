with open(r'../task-26/files/26_6759.txt') as file:
    N = int(file.readline())
    tovar = [int(i) for i in file]

tovar = sorted(tovar)
sale = N//3

minn = sum(tovar) - sum(tovar[::-1][2::3])
cus = sum(tovar) - sum(tovar[-sale:])



print(cus, minn )