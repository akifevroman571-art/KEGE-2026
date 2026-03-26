
with open(r'../task-9/files/14251.txt') as file:
    data = [list(map(int, i.split())) for i in file]


# 3 4 4 3 2 6 7
# cnt = [1, 1, 1, 2, 2,]
for pos, line in enumerate(data, start=1):
    cnt = [line.count(i) for i in set(line)]
    if sorted(cnt) == [1, 1, 1, 2, 2]:
        pov = [i for i in line if line.count(i) > 1]
        nechet = [i for i in line if i % 2 != 0]
        if sum(pov) <= sum(nechet):
            print(sum(line))
            break



