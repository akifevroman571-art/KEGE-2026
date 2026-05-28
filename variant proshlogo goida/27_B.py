from math import dist
def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]


with open(r'../variant proshlogo goida/27_B_23284.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1 = [dot for dot in dots if 0 < dot[0] < 13 ]
cluster_2 = [dot for dot in dots if 15 < dot[0] < 19]
cluster_3 = [dot for dot in dots if 19 < dot[0] < 31]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

b = dist(center_2, center_1)
b1 = dist(center_2, center_3)
b2 = dist(center_3, center_1)
print(min(b, b1,b2)*10000)
print(max(b, b1,b2)*10000)