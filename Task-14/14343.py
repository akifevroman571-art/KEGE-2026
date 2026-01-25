def c(n, sys):
    res = ''
    while n:
        res += str(n % sys)
        n //= sys
    return res[::-1]


num = c(5*343**2031 + 4*49**2142 - 3*7**111 + 7**222, 7)
print(sum(map(int, num)))



