with open(r'../task-17/files/17_21595.txt','r') as file:
    data = [int(i) for i in file]

ch3 = [i for i in data if len(str(abs(i))) == 4 and abs(i) % 10 == 3]

ans = []
for num1, num2 ,num3 in zip(data,data[1:],data[2:]):
    u1 = max(num1,num2, num3)
    u2 = num1+num2+num3 - min(num1, num2, num3) - u1
    if u1+u2 > (len(ch3))**2:
        ans.append(num1+num2+num3)

print(len(ans), max(ans))
