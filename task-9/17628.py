with open(r'../task-9/files/17628.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for line in data:
    ost = sum(line) - min(line) - max(line)
    maxmin = sum(line) - ost
    if maxmin <= ost:
        ans+=1
print(ans)