from math import prod

with open(r'.\files\17_11236.txt') as file:
    data = [int(i) for i in file]

min_2 = min(i for i in data if len(str(abs(i))) == 2) ** 2
max_1 = abs(max(i for i in data if str(i)[-1] == '1' and len(str(abs(i))) == 4))

ans = []
for num in zip(data, data[1:], data[2:]):
    u1 = sum(i > min_2 for i in num) == 2
    u2 = prod(map(abs, num)) % max_1 == 0
    if u1 and u2:
        ans.append(sum(map(abs, num)))
print(len(ans), max(ans))
