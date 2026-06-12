with open(r'files/26_23208.txt') as f:
    N = int(f.readline())
    details = []
    for num, line in enumerate(f, start=1):
        grind, paint = map(int, line.split())
        details.append([grind, 'G', num])
        details.append([paint, 'P', num])

details = sorted(details)
conveyor = [0] * N
last_id = 0
cnt_grind=0
for detail in details:
    if detail[2] not in conveyor:
        if detail[1] == 'G':
            conveyor[conveyor.index(0)] = detail[2]
            cnt_grind +=1
        else:
            conveyor[N-conveyor[::-1].index(0)-1] = detail[2]
        last_id = detail
print(last_id, cnt_grind)
