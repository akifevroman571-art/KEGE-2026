with open(r'../task-26/files/26_12113.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)

red_tracer = [max(i for i in boxes if i % 2 == 1)]
blue_tracer = [max(boxes, key=lambda x: (x%2==0, x))]

for box in boxes:
    if red_tracer[-1] % 2 != box % 2 and red_tracer[-1] - box >= 7:
        red_tracer.append(box)
    if blue_tracer[-1] % 2 != box % 2 and blue_tracer[-1] - box >= 7:
        blue_tracer.append(box)


print(len(red_tracer), red_tracer[-1])
print(len(blue_tracer), blue_tracer[-1])
