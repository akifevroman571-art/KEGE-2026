from re import *

with open(r'../task-24/files-24/24-314.txt') as f:
    data = f.readline()
num = r'([1-7][0-7]*|0)'
pattern = rf'(?<=F)({num}[+*])+{num}'

matches = [match.group() for match in finditer(pattern, data)]
print(matches)

ans = []

for match in matches:
    match = match.replace('+', ' + ')
    match = match.replace('*', ' * ')
    match = match.split()
    match = [str(int(match[i], 8)) if i % 2 == 0 else match[i] for i in range(len(match))]
    ans.append([len(match), eval(''.join(match))])

print(max(ans))

