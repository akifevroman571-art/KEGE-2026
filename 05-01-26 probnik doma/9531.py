from itertools import permutations

matrix = '345 35 128 156 124 478 68 367'.split()
graph = 'AB AC AZ BD BC CG DG DE EZ EJ JZ'.split()
print(*range(1, 9))
for i in permutations('ABCDEGZJ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
