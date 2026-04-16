from math import dist

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, d) for d in cluster)
        res.append([sum_dist, dot1])
    return min(res)[-1]
with open(r'./files/27_A_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
cluster_a1 = [d for d in dots if d[0] < 5]
cluster_a2 = [d for d in dots if d[0] >5 ]

center1 = center(cluster_a1)
center2 = center(cluster_a2)

print(max(center1[0], center2[0])*10000)
print(max(center1[1], center2[1])*10000)


with open(r'./files/27_B_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_b1 = [dot for dot in dots if 3< dot[1]<12]
cluster_b2 = [dot for dot in dots if 15< dot[1]<21]
cluster_b3 = [dot for dot in dots if 21< dot[1]<27]

center_B_min = center(min(cluster_b1, cluster_b2, cluster_b3 , key=len))
center_B_max = center(max(cluster_b1, cluster_b2, cluster_b3, key=len))

print(abs(center_B_min[0]-center_B_max[0])*10000)
print(abs(center_B_min[1]-center_B_max[1])*10000)