with open(r'..//task-17/files/17_18176.txt') as file:
    data = [int(i) for i in file]
ans=[]
min_4 = min(i for i in data if str(i)[-1] == '4' and i >= 0)
for num1, num2 ,num3 in zip(data, data[1:], data[2:]):
     if sum(map(int, str(abs(num1))))+sum(map(int, str(abs(num2))))+sum(map(int, str(abs(num3))))==min_4:
         ans.append(num1+num2+num3)
print(len(ans))
print(max(ans))
