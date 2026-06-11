with open(r'files/26_9847.txt') as f:
    N = f.readline()
    times = [list(map(int, i.split())) for i in f]

cnt=0
times = sorted(times)
time_line = [0] * 60 * 24

for time in times:
    for i in range(time[0], time[1]):
        time_line[i]+=1
print(time_line)
print(max(time_line))

for i in range(len(time_line)-1):
    if time_line[i]==time_line[i+1]==max(time_line):
        cnt+=1
print(cnt)
