# порядок выполнения операция алгебры логики
# Инверсия - not
# Конъюнкции - and
# Дизъюнкция - or
# Импликация - <=
# Эквивалентность - ==

# порядок выполнения операций Python
# ()
# **
# /, //, %, *
# +, -
# ==, !=, <, >, <=, >=
# not
# and
# or
# решение лесенкой
for a in range(2):
    for b in 0,1:
        for c in [0,1]:
            for d in(0, 1):
                f = (not a and not b) or (b == c) or d
                if f:
                    print(a, b, c, d)
                if not f:
                    print(a, b, c, d)
                print(a, b, c, d)

# args
def f1(a, b, c):
    return a+b+c
test = [1, 2, 3]
print(f1(*(test)))

# kwargs
def f2(a, b):
    return a / b


test2 = {'a':5, 'b':2}
print(f2(**test2))

# убийца второго задания
from itertools import product, permutations

def f(x, y, z, w):
    return (x or y) and not (y == z) and not w

for i in product((0, 1), repeat=4):
    table = [
        (1, i[0], 1, i[1]),
        (0, 1, i[2], 0),
        (i[3], 1, 1, 0)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
                print(*p)