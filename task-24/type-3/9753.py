with open(r'../files-24/24_9753.txt') as f:
    data = f.readline()
data = data.split('Y')
ans = 0
for i in range(len(data)-150):
    ans = max(ans, len('Y'.join(data[i:i+151])))
print(ans)