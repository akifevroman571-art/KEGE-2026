from math import dist
from itertools import *
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_B_29081.txt') as f:
    dots = []
    target = []
    for i in f:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if int(data[1]) >= 8 :
            target.append(list(map(float, [x, y])))

cluster_1 = [[d for d in dots if d[1] < 16],
             [d for d in target if d[1] < 16]]

cluster_2 = [[d for d in dots if 16 < d[1] < 22],
             [d for d in target if 16 < d[1] < 22]]

cluster_3 = [[d for d in dots if d[1] > 23],
             [d for d in target if d[1] > 23]]


clusters = [cluster_1, cluster_2, cluster_3]


B1 = min(dist(d1, d2) for cl1, cl2 in combinations(clusters, 2) for d1 in cl1[1] for d2 in cl2[1])

ans = [dist(d1, d2) for c in clusters for d1, d2 in combinations(c[1], 2)]
B2 = sum(ans) / len(ans)


print(B1 * 10000, B2 * 10000)
