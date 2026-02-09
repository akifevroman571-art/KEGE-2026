def fact(num):
    d = []
    while num % 2 ==0:
        d+=[2]
        num//=2
    i = 3
    while i < int(num**.5)+1:
        while num % i ==0:
            d+=[i]
            num//=i
        i+=2
    if num >2:
        d+=[num]
    return d
cnt = 0
for i in range(6086055+1, 10**20):
    d = fact(i)
    if len(d) == 2 and str(d[0]).count('6')  == str(d[1]).count('6') == 1:
        print(i, max(d))
        cnt+=1
        if cnt == 5:
            break

