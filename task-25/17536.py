def f (n):
    d = set()
    for i in range(2, int(n**0.5)+1):
        if n % i ==0:
            d |= {i, n//i}
    if len(d) >1:
        return min(d) +max(d)
    return 0
cnt = 0
for i in range(800001, 10**20):
    F = f(i)
    if F % 10 == 4:
        print(i, F)
        cnt+=1
        if cnt ==5:
            break


