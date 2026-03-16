with open(r'.\files\17_17530.txt') as file:
    data = [int(i) for i in file]

ans=[]
minn = min(data)

for num1, num2 in zip(data, data[1:]):
    if num1 % 55 == minn or num2 % 55 == minn:
        ans.append(num1 + num2)
print(len(ans))
print(min(ans))