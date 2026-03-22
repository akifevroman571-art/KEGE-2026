with open(r'../task-26/files/26_16390.txt') as file:
    S, N = map(int, file.readline().split())
    boxes = [int(i) for i in file]

boxes = sorted(boxes)
max1 = []
ans = []
for box in boxes:
    if sum(ans) + box <= S:
        ans.append(box)

ans = ans[:-1]
free_space = S - sum(ans)

print(len(ans)+1, max(i for i in boxes if i <= free_space))

