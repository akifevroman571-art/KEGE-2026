with open(r'files/26_24.txt') as f:
    S, N = map(int, f.readline().split())
    files = [int(i) for i in f]

files = sorted(files)
disk = []

for i in files:
    if sum(disk) + i <= S:
        disk.append(i)


disk = disk[:-1]

for i in files[::-1]:
    if sum(disk) + i <= S:
        disk.append(i)
        break
print(len(disk), disk[-1])



