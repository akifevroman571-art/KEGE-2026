with open(r'files/26_21598.txt') as f:
    N = f.readline()
    times = [list(map(int, i.split())) for i in f]

cnt=0
times = sorted(times)
time_line = [0] * (60 * 24+1)
ans1 = []
for time in times:
    for i in range(time[0], time[1]+1):
        time_line[i] +=1
ans2 = cnt = 0
for i in range(1, 24*60):
    if time_line[i] == time_line[i+1] != 0:
        cnt+=1
    elif time_line[i] != time_line[i+1]:
        ans1.append(i+1)
        cnt = 0
    ans2 = max(ans2, cnt)
print(ans1[-2]-1, ans2)








