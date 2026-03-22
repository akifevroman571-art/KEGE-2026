with open(r'../task-26/files/26.2_19727.txt') as file:
    M, N = map(int, file.readline().split())
    bidons = [int(i) for i in file]

bidons = sorted(bidons)
max1 = []
ans = []
for bid in bidons:
    if sum(ans) + bid <= M:
        ans.append(bid)

free_space = M - sum(ans[:-1])
print(len(ans), len([i for i in bidons if i > free_space]))


