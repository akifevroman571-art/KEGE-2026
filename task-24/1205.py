with open(r'.\files-24\24_1205.txt') as file:
    data = file.readline()


ans = 0
cnt = 0
for i in data:
    if i not in 'GWP':
        cnt +=1
    else:
        ans = max(cnt, ans)
        cnt = 0
ans = max(cnt, ans)
print(ans)