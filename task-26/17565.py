with open(r'files/26_17565.txt') as f:
    N, S = map(int, f.readline().split())
    students = []
    for i in f:
        ID, n1, n2, n3, interview = map(int, i.split())
        students.append([n1+n2+n3, interview, ID])

students = sorted(students, key=lambda x: (-x[0], -x[1], x[2]))
print(students[:S])





