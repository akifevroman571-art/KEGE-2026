from itertools import combinations

count = 0
with open(r'../task-9/files/19702.txt') as f:
    for line in f:
        nums = [int(x) for x in line.split()]
        for c in combinations(nums, 4):
            if len(set(c)) == 4:
                c = sorted(c)
                if c[1] - c[0] == c[2] - c[1] == c[3] - c[2]:
                    count += 1
                    break
print(count)
