from itertools import *

# permutations - формирует все возможные перестановки элементов коллекции
alph = '122'
for val in  permutations(alph):
    val = ''.join(val)
    print(val)

# product - формирует ве возможные комбинации определенной длины
alph2 = '123'
for val in product(alph2, repeat=3):
    val = ''.join(val)
    print(val)



#enumerate - номерует элементы последовательности начиная от start
alph3 = '123'
res = enumerate(alph3, start=1)
print(*res)