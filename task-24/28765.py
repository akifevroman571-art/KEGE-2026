with open(r'files-24/24_28765.txt') as f:
    data = f.readline()
data = data.replace('BC', 'B C')
data = data.split()
ans= 0
for i in range(len(data)-180):
    ans = max(ans, len(''.join(data[i: i + 181])))

print(ans)