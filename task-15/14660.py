from itertools import combinations
def f(x):
    P = 16 <= x <= 84
    Q = 27 <= x <= 43
    A = A1 <= x <= A2
    return (A <= P) or Q
lineA = [16, 27, 43, 84]
linex = [16.5, 27.5, 43.5]

ans = []

for A1, A2 in combinations(lineA, 2):
    if all(f(x)for x in linex):
        ans.append([A2-A1])
print(max(ans))
