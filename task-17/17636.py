with open(r'.\files\17_17636.txt') as file:
    data = [int(i) for i in file]

ans = []
maxx = max(int(i) for i in data)

for num1, num2, num3 in zip(data, data[1:], data[2:]):
    if (num1 % 10 == 3 and len(str(num1)) == 3) or (num2 % 10 == 3 and len(str(num2)) == 3) or (num3 % 10 == 3 and len(str(num3)) == 3):
        if num1 + num2 + num3 < maxx:
            ans.append(num1+num2+num3)
print(len(ans))
print(max(ans))