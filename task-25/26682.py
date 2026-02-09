def fact(num):
    d = []
    while num % 2 == 0:
        d+=[2]
        num//=2
    i =3
    while i < int(num**.5)+1:
        while num % i == 0:
            d+=[i]
            num//i
        i+=2
    if num >2:
        d+=[num]
    return d

def t(num):
    dels= []
    for i in range(1, int(num**.5)+1):
        if i * i == num:
            dels.append(i)
        elif num % i == 0:
            dels.append(i)
            dels.append(num//i)
    return dels

cnt = 0
for i in range(5200000+1, 10**20):
    d = fact(i)
    if len(dels) == 90 and len(d) == 9:
        print(i, max(d))
        cnt+=1
        if cnt == 5:
            break
