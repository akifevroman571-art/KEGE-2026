def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def f(num):
    d = []
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            if is_prime(i):
                d += [i]
            if is_prime(num // i):
                d+=[num//i]
    if len(d) == 2 and d[0] * d[1] == num:
        if str(d[0]).count('5') == str(d[1]).count('5') == 1:
            return max(d)
    return 0
cnt = 0
for n in range(1324728, 10**20):
    m = f(n)
    if m:
        print(n, m)
        cnt +=1
        if cnt ==5:
            break







