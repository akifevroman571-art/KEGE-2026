with open(r'../task-26/files/26_4660.txt') as file:
    N = int(file.readline())
    tovar = [int(i) for i in file]

tovar = sorted(tovar)
sale = N // 4

sale = N // 4
one_check = sum(tovar) - sum(tovar[:sale]) // 2

many_cheks = sum(tovar) - sum(tovar[::-1][3::4]) // 2

print(one_check, many_cheks)
