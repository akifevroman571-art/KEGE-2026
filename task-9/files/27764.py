with open(r'27764.txt') as f:
    data = [list(map(int,i.split())) for i in f]

cnt = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1,1,1,1,1]:
        if (max(line) + min(line))*2 == sum(line) -max(line) - min(line):
            cnt+=1
print(cnt)

