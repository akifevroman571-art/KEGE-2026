with open(r'../KEGE-05-04/file/17 (1).txt') as file:
    data = [int(i) for i in file]
mx2 = max(i for i in data if len(str(i)) == 2)
ans = []
for num1, num2 in zip(data, data[1:]):
    if len(str(num1)) == 2 or len(str(num2))==2:
        if (num1+num2) % mx2 == 0:
            ans.append(num1+num2)
print(len(ans), max(ans))

