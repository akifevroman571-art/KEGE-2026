with open(r'../files-24/24_9753.txt') as f:
    data = f.readline()

ans = 0
l = 0
r = 0
cnt = 0

while r < len(data)-1:
    if cnt <= 150:

        if data[r] == 'Y': cnt+=1
        r += 1
    else:
        while cnt >150:
            if data[l] == 'Y': cnt -= 1
            l+=1
        ans = max(ans, r - l - 1)
print(ans)


