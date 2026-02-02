def is_prime(num):
    if num < 2: return false
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(n**0.5)+1):
        if num % i ==0:
            if is_prime(i):
                d |= {i}
            if is_prime(num // i):
                d |= {num // i}
    if len(d) > 1:
        m = max(d) + min(d)
        if m > 60000 and str(m) == str(m)[::-1]:
            return m
    return 0
cnt = 0
for n in range(5400000, 10**20):
    m = f(n)
    if m:
        print(n, m)
        cnt +=1
        if cnt == 5:
            break