with open(r'../files-24/24_20909.txt') as f:
    data = f.readline()
data = data.replace('AB', 'A B')
data = data.split()
ans = 0
for i in range(len(data)-100):
    ans = max(ans, len(''.join(data[i:i + 101])))
print(ans)