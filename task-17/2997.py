with open(r'.\files\17_2997.txt') as file:
    data = [int(i) for i in file]

ans = []

data_3 = [int(str(abs(i))[1]) for i in data if len(str(abs(i))) == 3]
most_common = max((data_3.count(i), i) for i in set(data_3))[1]
for num in zip(data, data[1:]):
    if any(abs(i) % 10 == most_common for i in num):
        ans.append(sum(num))
print(len(ans))
print(max(ans))

