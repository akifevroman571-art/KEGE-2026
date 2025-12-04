cnt = 0
from itertools import *
for val in product('НИЧЬЯ', repeat=7):
    val=''.join(val)
    if val.count('И') + val.count('Я') == 2 and 'ИЯ' not in val and 'ИИ' not in val and 'ЯИ' not in val and 'ЯЯ' not in val:
        cnt+=1
print(cnt)