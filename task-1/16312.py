from itertools import *

matrix = '37 57 147 37 26 57 12346'.split()
graph = 'AC AD AG CD GD DB DE BF EF'.split()
print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)