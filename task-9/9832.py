with open(r'../task-9/files/9832.txt') as file:
    data = [list(map(int, i.split()))for i in file]

for line in data:
    u1 = [line.count(i) for i in line]
    if u1.count(2) == 4 and u1.count(1) == 3:
        if line.count(max(line)) == 1:
            print(sum(line))
            break

