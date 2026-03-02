from itertools import *

def f(x):
    B = 24 <= x <= 90
    C = 47 <= x <= 115
    A = A1 <= x <= A2
    return C <= (((not A) and B) <= (not C))
linea = [24,47,90,115]
linex=[24.5,47.5,90.5]
ans = []
for A1, A2 in combinations(linea, 2):
    if all(f(x) for x in linex):
         ans.append(A2 - A1)
print(min(ans))