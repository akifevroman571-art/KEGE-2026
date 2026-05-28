
def is_prime(num):
    if num <2: return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
def f(num):
    d = []
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            if is_prime(i):
                d+=[i]
            if is_prime(num // i):
                d+=[num // i]
    if len(d) > 1:
        M = min(d) + max(d)
        if M > 60000 and str(M) == str(M)[::-1]:
            return M
    return 0
cnt = 0

for n in range(5400000, 10**20):
    m = f(n)
    if m > 0:
        cnt+=1
        print(n, m)
        if cnt==5:
            break

