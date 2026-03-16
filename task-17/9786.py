with open(r'.\files\17_9786.txt') as file:
    data = [int(i) for i in file]

ans = []

max_25 = max(i for i in data if abs(i) % 100 == 25)

for num1, num2, num3 in zip(data, data[1:], data[2:]):
    if ((len(str(abs(num1)))==4) + (len(str(abs(num2)))==4) + (len(str(abs(num3)))==4)) <= 2:
        if num1 + num2 + num3 <= max_25:
            ans.append(num1+num2+num3)
print(len(ans))
print(max(ans))




