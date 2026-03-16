with open(r'.\files\17_2473.txt') as file:
    data = [int(i) for i in file]
ans = []
for num1, num2 in zip(data, data[1:]):
    if num1 % 7 == 0 or num2 % 7 == 0:
        if str(num1)[-1] == '3' or str(num2)[-1] == '3':
            ans.append(num1+num2)
print(len(ans))
print(min(ans))


