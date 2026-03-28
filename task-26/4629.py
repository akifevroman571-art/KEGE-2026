with open(r'../task-26/files/26_4629.txt') as file:
    N = int(file.readline())
    tovar = [int(i) for i in file]

tovar = sorted(tovar)
sale = N // 4

cus = sum(tovar) - sum(tovar[-sale:]) // 2
store = sum(tovar) - sum(tovar[:sale]) // 2
print(cus, store)

