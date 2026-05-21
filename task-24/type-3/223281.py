with open(r'../files-24/24_23281.txt') as f:
    data = f.readline()
ans = 0
data=data.split('Y')
for i in range(len(data)-80):
    line = 'Y'.join(data[i:i+81])
    if line.count('2025') >= 90:
        ans = max(ans, len(line))
print(ans)
