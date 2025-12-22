with open(r'.\files-24\24_1273.txt') as file:
    data = file.readline()

cnt = 0
ans = 2
for i in range(len(data)-2):
    if data[i:i+3] != 'XYZ':
        cnt +=1
    else:
        ans = max(cnt, ans)
        cnt =2
ans = max(cnt, ans)
print(ans)
