with open(r'files/26_23283.txt') as f:
    K = int(f.readline())
    N = int(f.readline())
    times = [list(map(int, i.split())) for i in f]
pos=0
cnt = 0
times = sorted(times)
time_line = [0] * K
for time in times:
    for i in range(K):
        if time_line[i] < time[0]:
            time_line[i] = time[1]
            cnt+=1
            pos = i+1
            break
print(cnt, pos)


