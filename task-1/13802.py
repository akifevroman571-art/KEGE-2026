from itertools import *
matrix = '367 568 18 58 247 127 156 234'.split()
graph = 'AE AF ED FD DB FC EH HB HG CG GB'.split()
print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print(10+11)