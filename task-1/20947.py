from itertools import *

matrix = '267 157 468 356 248 134 12 35'.split()
graph = 'AB AC CB BG BD GJ DJ DU DE GU EU'.split()
print(*range(1, 9))
for i in permutations('ABCDEJUG'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
