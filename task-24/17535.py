with open(r'../task-24/files-24/24_17535.txt') as f:
    data = f.readline()

data = data.replace('CD', 'C D')
data = data.split()
ans = 0
for i in range(len(data)-160):
    ans = max(ans, len(''.join(data[i:i + 161])))
print(ans)