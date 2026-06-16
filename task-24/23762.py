with open('files-24/24_23762.txt') as f:
    data = f.readline()

data = data.split('Y')

ans = 0
for i in range(len(data)-80):
    a = 'Y'.join(data[i: i+81])
    if a.count('2025') >= 90:
        ans = max(ans, len(a))
print(ans)

