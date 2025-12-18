from itertools import permutations

matrix = '38 58 146 36 27 347 568 127'.split()
graph = 'AH AE ED DB EB BG HG GF FC HC'.split()

print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)