with open(r'files/26_2_23175 (1).txt') as f:
    N, M = map(int, f.readline().split())
    loads = [int(f.readline()) for i in range(N)]
    containers = [int(f.readline()) for i in range(M)]

loads = sorted(loads)
last_container=0
containers = sorted(containers)
cnt = 0
loaded = []
for load in loads:
    for container in containers:
        if container - load >= 0:
            loaded.append(load)
            last_container = container
            containers.remove(container)
            break


loaded = loaded[:-1]
for load in loads[::-1]:
    if last_container - load >= 0:
        loaded.append(load)
        break
print(len(loaded), loaded[-1] - loaded[-2])

