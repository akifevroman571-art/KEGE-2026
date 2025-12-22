from itertools import permutations


matrix = '24 146 56 1267 36 23457 46'.split()
graph = 'AB AC BC BD BG BE DE GE EK EG GK'.split()


print(*range(1, 8))
for i in permutations('ABCDEGK'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)