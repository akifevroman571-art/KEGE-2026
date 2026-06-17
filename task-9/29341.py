with open(r'files/29341.txt') as f:
    data = [list(map(int, i.split())) for i in f]
cnt = 0
for line in data:
    if max(line) < sum(line) - max(line):
        if min(line) + max(line) != sum(line) - min(line) - max(line):
            cnt+=1
print(cnt)
