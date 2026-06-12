with open(r'files/26_9847.txt') as f:
    N = f.readline()
    times = [list(map(int, i.split())) for i in f]

cnt=0
times = sorted(times)
time_line = [0] * 60 * 24



print(time_line)

print(len(times))