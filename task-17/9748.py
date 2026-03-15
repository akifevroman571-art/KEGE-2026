with open(r'..\files\17_9748.txt') as file:
    data = [int(i) for i in file]
ans = []
max_15 = max(i for i in data if abs(i) % 100 == 15)
for num1, num2, num3  in zip(data, data[1:], data[2:]):
    u1 = [len(str(num1)), len(str(num2)), len(str(num3))].count(4) == 1
    u2 = num1 + num2 + num3 >= max_15
    if u1*u2:
        ans+=[(num1+num2+num3)]
print(len(ans), max(ans))
