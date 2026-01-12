from itertools import *

matrix = '67 567 457 35 234 12 123'.split()
graph = 'AB AC BC BD CE EG GF DE DF'.split()
print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
