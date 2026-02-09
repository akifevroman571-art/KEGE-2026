ans = []
for n in range(1, 30):
    r = f'{n:b}'
    a = sum(map(int, r))
    if a % 2 == 0:
        r = '10' + r[:-2] + '00'
    else:
        r = '11' + r[:-2] + '11'
    r = int(r,2)
    if n < 30:
        ans.append(r)
print(ans)
