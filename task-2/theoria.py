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