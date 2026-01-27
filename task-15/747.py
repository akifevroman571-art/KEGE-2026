from itertools import combinations

def f(x):
    P = 43 <= x <= 49
    Q = 44 <= x <= 53
    return (A1 <= P) or Q
line_A = [43, 44, 49, 53]
line_X = [44, 45, 50]
ans=[]
for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_X):
        ans.append(A2 - A1)
print(max(ans))