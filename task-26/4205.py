with open(r'files/26_4205.txt') as f:
    N = int(f.readline())
    frees = []
    for i in f:
        free = list(map(int, i.split()))
        frees.append(free)
frees = sorted(frees, key=lambda x: (-x[0], x[1]))
ans = []
for i in range(len(frees)-1):
    if frees[i][0] == frees[i+1][0]:
        if frees[i+1][1] - frees[i][1] ==13:
            print(frees[i][0], frees[i][1]+1)
            break
