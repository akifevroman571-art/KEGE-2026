ans = []
for n in range(1, 10000):
    r = f'{n+2:b}'
    r = r + str(sum(map(int, r))%2)
    r = r + str(sum(map(int, r))%2)
    r = int(r, 2)
    if r < 61:
        ans.append([n, r])
print(ans)

