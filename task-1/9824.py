from itertools import permutations

matrix = '346 45 16 125 247 137 56'.split()
graph = 'FD DG GE DE EC CA CB BA AF'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)