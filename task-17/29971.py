with open(r'files/17_29971.txt') as f:
    data = [int(i) for i in f]

max_33 = max(i for i in data if str(i)[-2:] == '33')

ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = len(str(abs(num1))) == 2
    u2 =len(str(abs(num2))) == 2
    u3 = len(str(abs(num3))) == 2
    if u1 + u2 + u3 == 2:
        if (num1+num2+num3) ** 2 < max_33:
            ans.append([num1+num2+num3])
print(len(ans))
print(max(ans))
