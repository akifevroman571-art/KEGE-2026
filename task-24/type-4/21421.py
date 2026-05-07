from re import *


with open(r'../files-24/24_21421.txt') as f:
    data = f.readline()

pattern = fr'[1-9AB][0-9AB]*[02468A]'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
