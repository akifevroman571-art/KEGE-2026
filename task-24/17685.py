from re import finditer

with open(r'files-24/24_17685.txt') as f:
    data = f.readline()


num = r'(0|([1-9][0-9]))*'
pattern = r'[num]([*+]{num})'
matches = [match.group() for match in finditer(pattern, data)]

ans = 0
for number in matches:
    len_number = len(number)
    if eval(number) == 0:





