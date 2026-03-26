# По умолчанию глубина рекурсии не может превышать 1000
# Мы можем расширить кол-во шагов при помощи:
from sys import setrecursionlimit

steps_amount = 2000
setrecursionlimit(steps_amount)

# Значение steps_amount высчитывается по формуле:
# steps_amount = ceil(N / step) + 1, где
# N - самое большое число, которое передается функции.
# step - значение, на которое увеличивается/уменьшается число при вызове нового шага рекурсии.
# Данный способ ок, если steps_amount не более двух тысяч, в других случаях нужен lru_cache
# пример
# номер 21415
from sys import setrecursionlimit

def f(n):
    if n <= 5: return 1
    return n+f(n-2)

steps_amount = 2000
setrecursionlimit(steps_amount)
print(f(2126)-f(2122))
# номер 21415
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n < 43: return g(n+4)
    return 2*f(n-2)-f(n-4)+2
@lru_cache(None)
def g(n):
    if n < 11240: return g(n+3)+2
    return q(n)
@lru_cache(None)
def q(n):
    if n < 21: return n+4
    return q(n-4)+2
for i in range(20, 11240):
    q(i)
for i in range(11240, 42, -1):
    g(i)
print(f(2026))