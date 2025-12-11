from itertools import permutations

cnt = 0
for val in permutations('ПРОБНИК'):
    val = ''.join(val)
    if val[0] not in 'ОИ' and val[-1] not in 'ОИ' and \
            'ОИ' not in val and 'ИО' not in val:
        cnt += 1
print(cnt)
