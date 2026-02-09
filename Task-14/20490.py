for x in range(1, 2006):
    a = str(4**163 * 5 + 12**62 -x)
    ans = []
    while a:
        if a.count('1') < a.count('4'):
            ans.append(x)
print(max(ans))