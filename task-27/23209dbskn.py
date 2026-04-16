from math import dist

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, d) for d in cluster)
        res.append([sum_dist, dot1])
    return min(res)[-1]
with open(r'./files/27_A_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 30:
        clusters.append(cluster)

print([len(cluster) for cluster in clusters])

centers = [center(cluster) for cluster in clusters]

print(max(centers, key=lambda x: x[0])[0] * 10000)

print(max(centers, key=lambda x: x[1])[1] * 10000)

from math import dist

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, d) for d in cluster)
        res.append([sum_dist, dot1])
    return min(res)[-1]
with open(r'./files/27_B_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 30:
        clusters.append(cluster)

print([len(cluster) for cluster in clusters])

centers = [center(cluster) for cluster in clusters]

center_B_min = center(min(clusters, key=len))
center_B_max = center(max(clusters, key=len))

print(abs(center_B_min[0]-center_B_max[0])*10000)
print(abs(center_B_min[1]-center_B_max[1])*10000)


