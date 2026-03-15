with open(r'..\task-17\files\17_12249.txt') as file:
    data = [int(i) for i in file]
max_tri = max(i for i in data if len(str(abs(i))) == 5 and str(i).endswith('3'))
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = num1 % 3 == 0
    u2 = num2 % 3 == 0
    u3 = num3 % 3 == 0
    u4 = num1+num2+num3 <= max_tri
    if u1 + u2 +u3 + u4 >= 1 and any([u1, u2, u3, u4]) and (u1 or u2, u3, u4):
        ans += (num1 + num2 + num3)
print(len(ans))
print(max(ans))
