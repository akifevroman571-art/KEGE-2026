with open(r'files/26_21719.txt') as f:
    N = int(f.readline())
    students ={}
    for l in f:
        ID, task = map(int, l.split())
        if ID not in students:
            students[ID] = {task}
        else:
            students[ID] |= {task}
ans=[]

for ID in students:
    tasks = sorted(students[ID])
    cnt=1
    for i in range(len(tasks)-1):
        if tasks[i+1] - tasks[i] == 2:
            cnt+=1
        else:
            cnt=1
        ans.append([cnt, ID])


print(max(ans, key=lambda x: (x[0], -x[1])))



