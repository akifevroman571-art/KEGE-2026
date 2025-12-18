from itertools import permutations

matrix = '247 148 578 126 38 47 136 235'.split()
graph = 'FH HB HA BA AE EG EC GC GF CD DF'.split()
print(*range(1, 9))
for i in permutations('ABCDEFGH'):
     if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
         print(*i)
