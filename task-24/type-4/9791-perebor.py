from string import printable

with open(r'../files-24/24_9791.txt') as f:
    data = f.readline().lower()

ans = 0
checkpoint = 0


for i in range(len(data)):
    if data[i] in printable[:16]:
        cnt = 0
        for j in range(i, len(data)):
            if data[j] in printable[:16]:
                cnt+=1
            else:
                checkpoint = j
                break
        ans = max(ans, cnt)

print(ans)





