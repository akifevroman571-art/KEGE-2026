from itertools import permutations


matrix = '256 13467 2456 237 136  1235 24'.split()
graph = 'AB BE EF FD DC CA ED AG BG CG DG'.split()


print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)