from math import dist

def center(cluster):
    res=[]
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'./files/27_A_29074.txt') as f:
    dots = []
    target = []
    for i in f:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z':
            target.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] <8]
cluster_2 = [d for d in dots if d[1] >8]

trg_cl1 = [d for d in target if d[1] <8]
trg_cl2 = [d for d in target if d[1] >8]

print(len(trg_cl1))
print(len(trg_cl2))


