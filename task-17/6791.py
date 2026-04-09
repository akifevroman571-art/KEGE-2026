with open(r'..//task-17/files/17_6791.txt') as file:
    data = [int(i) for i in file]

min68 = min(i for i in data if abs(i) // 100 == 68)
ans=[]
for num1, num2 in zip(data, data[1:]):
    if abs(num1 % 100) == 68 or abs(num2 % 100 == 68):
       if num1**2+num2**2 >= min68**2:
           ans.append(num1**2+num2**2)

print(len(ans))

print(max(ans))