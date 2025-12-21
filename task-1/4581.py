from itertools import permutations


matrix = '37 367 125 56 34 247 126'.split()
graph = 'CG GE EB ED DA BA BF AF FC'.split()


print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print(13 + 53)