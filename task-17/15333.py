with open(r'..//task-17/files/17_15333.txt') as file:
    data = [int(i) for i in file]

max_19 = max(i for i in data if i % 19 == 0)
ans= []
for num1, num2 in zip(data, data[1:]):
    if num1 > max_19 or num2 > max_19:
        ans.append(num1+num2)
print(len(ans))
print(max(ans))
