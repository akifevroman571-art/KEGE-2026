from itertools import *
def f(x):
    P = 15<= x<=40
    Q = 21<=x<=63
    A = A1<=x<=A2
    return P <= ((Q and (not A)) <= (not P))
Linea=[15,21,40,63]
linex=[16,22,41]

for A1, A2 in permutations(linex, 2):
    if all(f(x) for x in range(1, 1000)):
        print(A2-A1)
        break
