with open(r'../files-24/24_2942.txt') as file:
    data = file.readline()


ans = 0
cnt = 0
i = 0

while i < len(data) - 1:
    if data[i:i+2] in 'AB AC':
        cnt+=1
        i += 2
    else:
        cnt = 0
        i +=1
    ans = max(ans, cnt)
print(ans)

