with open(r'files/26_17881.txt') as f:
    N = int(f.readline())
    students_0 = []
    students_3 = []
    for i in f:
        ID, *exs = map(int, i.split())
        if exs.count(2) == 0:
            students_0.append([sum(exs)/4, ID])
        elif exs.count(2) == 3:
            students_3.append([sum(exs)/4, ID])

students_0 = sorted(students_0, key=lambda x: (-x[0], x[1]))


students_3 = sorted(students_3, key=lambda x: (-x[0], x[1]))
print(students_0[:N//4][-1][1], students_3[0][1])
