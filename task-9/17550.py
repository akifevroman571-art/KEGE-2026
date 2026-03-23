with open(r'../task-9/files/17550.txt') as file:
    data = [list(map(int, i.split())) for i in file]
ans=0
for line in data:
    cnt = [line.count(i) for i in set(line)]
    if sorted(cnt) == [1,1,1,3]:
        pov = [i for i in line if line.count(i)>1]
        nepov = [i for i in line if line.count(i)==1]
        if (sum(pov))**2 > (sum(nepov))**2:
            ans+=1
print(ans)
