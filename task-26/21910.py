with open(r'files/26_21910.txt') as f:
    N = int(f.readline())
    boxes = {int(i) for i in f}
boxes = sorted(boxes, reverse=True)
last_box=boxes[0]
cnt=1
for i in boxes:
    if last_box-i >= 9:
        last_box=i
        cnt+=1
print(cnt,last_box)


