with open(r'../task-26/files/26_16390.txt') as file:
    S, N = map(int, file.readline().split())
    boxes = [int(i) for i in file]

boxes = sorted(boxes)

ans = []
for box in boxes:
    if sum(ans) + box <= S:
        ans.append(box)

ans.pop()
for box in boxes[::-1]:
    if sum(ans) + box <= S:
        ans.append(box)
        break
print(len(ans), max(ans))
print(ans)