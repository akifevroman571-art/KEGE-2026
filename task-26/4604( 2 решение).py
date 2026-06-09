with open(r'files/26_4604.txt') as f:
    N = int(f.readline())
    boxes = [int(i) for i in f]

boxes = sorted(boxes)[::-1]
posl_box = boxes[0]
cnt = 1

for i in boxes:
    if posl_box - i >= 3:
        posl_box = i
        cnt+=1
print(cnt, posl_box)