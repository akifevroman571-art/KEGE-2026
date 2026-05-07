from re import *

with open(r'../files-24/24_23206.txt') as f:
    data = f.readline()

pattern = r'[02468]([^S02468]*S){35}[^S02468]*'

matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))