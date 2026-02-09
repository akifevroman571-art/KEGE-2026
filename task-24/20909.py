with open(r'.\files-24\24_20909.txt') as file:
    data = file.readline()
ans = 0
for i in range(len(data) - 101):
    if i == 0 or i == len(data)-101:
        ans = max(ans, len('AB'.join(data[i:i+101]))+1)
    else:
        ans = max(ans, len('AB'.join(data[i:i + 101]))+2)
print(ans)