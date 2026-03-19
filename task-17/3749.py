from math import prod

with open(r'.\files\17_3749.txt') as file:
    data = [int(i) for i in file]
sqrt_max = max(i for i in data if i ** 0.5 == int(i ** 0.5)) * 3

ans = []

for num in zip(data, data[1:]):
    u1 = prod(num) ** .5 % 1 == 0
    u2 = any(i <= sqrt_max for i in num)
    if u1 and u2:
        ans.append(prod(num) ** .5)
print(len(ans), max(ans)+min(ans))
