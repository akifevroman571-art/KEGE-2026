def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

with open(r'.\files\17_9993.txt') as file:
    data = [int(i) for i in file]

cnt = 0
ans = []
maxx = max(abs(i) for i in data if abs(i) % 100 == 17)

for num1, num2 in zip(data, data[1:]):
    if is_prime(num1) + is_prime(num2) == 1 and abs((num1+num2)) % maxx == 0:
        cnt+=1
        ans.append(num1*num2)
print(cnt)
print(max(ans))




