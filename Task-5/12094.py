ans = []
for n in range(1, 100000):
    R = f'{n:b}'
    if n % 8 ==0:
        R = R + R[-2:]
    else:
        R = R + f'{(n % 8)*2:b}'
    R = int(R, 2)
    if R > 3000:
        ans.append(n)
print(min(ans))

