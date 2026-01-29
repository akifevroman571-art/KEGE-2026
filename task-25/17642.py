
def f(n):
    d = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            d |= {i, n //i}
    d_9=[]
    for  i in sorted(d):
        if i != 9 and i % 10 == 9:
            d_9 += [i]
    if d_9:
        return min(d_9)
    return 0
cnt = 0
for n in range(800001, 10**20):
    F = f(n)
    if F:
        print(n, F)
        cnt +=1
        if cnt==5:
            break





