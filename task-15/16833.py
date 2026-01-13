from itertools import combinations

def f(x):
    P = 25 <= x <= 73
    Q = 75 <= x <= 118
    A = A1 <= x <= A2
    return (A and not Q) <= (P or Q)
ans = []
lineA = [25, 73, 75, 118]
lineX = [55, 74, 100]
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(A2-A1)
print(max(ans))