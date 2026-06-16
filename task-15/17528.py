from itertools import *
def f(x):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = A1 <= x <= A2
    return P <= ((Q and (not A)) <= (not P))
ans = []
lineA = [15,21,40,63]
lineX = [16,22,42]
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(A2-A1)
print(ans)
