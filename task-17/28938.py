with open(r'files/17_28938.txt') as f:
    data = [int(i) for i in f]

mx = max(i for i in data if str(i)[-2:] == '28')
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = len(str(abs(num1))) == 3
    u2 = len(str(abs(num2))) == 3
    u3 = len(str(abs(num3))) == 3
    if u1+u2+u3 >= 1:
        if (num1+num2+num3) // 3 > 0:
            if (num1+num2+num3) // 3 < mx:
                ans.append([num1+num2+num3])
print(len(ans), max(ans))