from math import dist
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot ,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_B_29080.txt') as f:
    dots = []
    target = []
    for i in f:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L':
            target.append(list(map(float, [x, y])))


cluster_1 = [[d for d in dots if d[1] < 16],
             [d for d in target if d[1] < 16]]

cluster_2 = [[d for d in dots if 16 < d[1] < 22],
             [d for d in target if 16 < d[1] < 22]]

cluster_3 = [[d for d in dots if d[1] > 23],
             [d for d in target if d[1] > 23]]

print(len(cluster_1[1]))

print(len(cluster_2[1]))

print(len(cluster_3[1]))

B1 = dist(center(cluster_1[0]), center(cluster_3[0]))
print(B1*10_000)


B2 = [dist(d1, d2) for d1 in cluster_1[1] for d2 in cluster_2[1]]+\
      [dist(d2,d3) for d2 in cluster_2[1] for d3 in cluster_3[1]]+\
       [dist(d1,d3) for d1 in cluster_1[1] for d3 in cluster_3[1]]
print(max(B2)*10000)

