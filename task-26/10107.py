with open(r'files/26_10107.txt') as f:
    N = int(f.readline())
    events = [list(map(int, i.split())) for i in f]

events = sorted(events, key=lambda x: (x[1], x[0]))
last_event = events[0]
cnt=1
ans = []
for i in events:
    if i[0] - last_event[1] >= 0:
        cnt+=1
        last_event = i
        ans.append(last_event)
print(cnt, ans)


