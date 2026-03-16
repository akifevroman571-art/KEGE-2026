with open(r'..\task-17\files\17_12249.txt') as file:
    data = [int(i) for i in file]
max_tri = max(i for i in data if len(str(abs(i))) == 5 and str(i).endswith('3'))
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = abs(num1) % 10 == 3
    u2 = abs(num2) % 10 == 3
    u3 = abs(num3) % 10 == 3
    u4 = num1+num2+num3 <= max_tri
    if any([u1, u2, u3]) and u4:
        ans.append(num1 + num2 + num3)
print(len(ans))
print(max(ans))

