from math import dist

def center(cluster):
    res=[]
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'./files/27_A_28766.txt') as f:
    dots = []
    target = []
    for i in f:
        x, y, data = i.replace(',', '.').split()
        dots. append(list(map(float, [x, y])))
        if data[0] == 'Y' and data[2:].rstrip() == 'III':
            target.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] <8]
cluster_2 = [d for d in dots if d[1] >8]


# print(len(cluster_2)) - наименьшее кол-во точек
center_2 = center(cluster_2)
ans = [dist(center_2, d) for d in target]
print(min(ans)*10000)
print(max(ans)*10_000)








