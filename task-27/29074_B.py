from math import dist

def center(cluster):
    res=[]
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'./files/27_B_29074.txt') as f:
    dots = []
    target = []
    for i in f:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L' and data[2:] == 'V':
            target.append([list(map(float, [x,y]))])

cluster_1 = [d for d in dots if d[0] > 20]
cluster_2 = [d for d in dots if d[1] <8 and d[0] < 23]
cluster_3 = [d for d in dots if d[0] < 23]

