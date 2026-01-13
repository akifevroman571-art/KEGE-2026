from itertools import combinations

def f(x):
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = A1 <= x <= A2
    return (not(C or J)) <= (not A)
ans = []
lineA = [48, 83, 94, 100]
lineX = [60, 85, 97]
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(A2-A1)
print(max(ans))
