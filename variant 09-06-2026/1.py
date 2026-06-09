from itertools import *

matrix = '68 568 457 35 235 12 38 127'.split()
graph = 'AB AD AH BC BE CD EG EF FG GH'.split()

print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)