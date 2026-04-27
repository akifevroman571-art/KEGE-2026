from math import dist
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot ,d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_A_29080.txt') as f:
    dots = []
    target = []
    for i in f:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L' and data[1] == '3':
            target.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] <8]


cluster_2 = [d for d in dots if d[1] >8]



print(len(cluster_1))
print(len(cluster_2))
# кластер 2 наименьший

center_2 = center(cluster_2)
center_1 = center(cluster_1)
ansA1 = []
ansA2= []
for d in target:
    ansA1.append(dist(center_2, d))

for d in target:
    ansA2.append(dist(center_1, d))

print(max(ansA1)*10_000)
print(max(ansA2)*10_000)




