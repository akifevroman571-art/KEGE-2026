with open(r'files/17_29349.txt') as f:
    data = [int(i) for i in f]

mn = min(i for i in data if i > 0 and i % 123 == 0)
print(mn)
ans = []
for num1, num2 in zip(data, data[1:]):
    if num1 + num2 < mn:
        ans.append([num1+num2])
print(len(ans), max(ans))
