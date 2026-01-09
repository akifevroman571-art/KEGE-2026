from itertools import *

matrix = '26 147 456 236 37 134 25'.split()
graph = 'AB AD AG BG BC CD DE EF FG'.split()
print(*range(1,8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)