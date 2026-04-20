from math import dist
def center(cluster):
    res=[]
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, d) for d in cluster)
        res.append([sum_dist, dot1])
    return max(res)[-1]

with open(r'./files/27.17.A_19566.txt') as f:
    dots = [list(map(float, i.split())) for i in f]
eps = 1
cls = []
while dots:
    cl = [dots.pop()]
    for dot in cl:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cl.append(d)
                dots.remove(d)
    if len(cl) > 4:
        cls.append(cl)
print([len(cl) for cl in cls])

edges = [center(cl) for cl in cls]

print(int(abs(sum(e[0] for e in edges)/ len(edges)*10000)))
print(int(abs(sum(e[1] for e in edges)/ len(edges)*10000)))




from math import dist
def center(cluster):
    res=[]
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, d) for d in cluster)
        res.append([sum_dist, dot1])
    return max(res)[-1]

with open(r'./files/27.17.B_19566.txt') as f:
    dots = [list(map(float, i.split())) for i in f]
eps = 1
cls = []
while dots:
    cl = [dots.pop()]
    for dot in cl:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cl.append(d)
                dots.remove(d)
    if len(cl) > 4:
        cls.append(cl)
print([len(cl) for cl in cls])

edges = [center(cl) for cl in cls]

print(int(abs(sum(e[0] for e in edges)/ len(edges)*10000)))
print(int(abs(sum(e[1] for e in edges)/ len(edges)*10000)))




