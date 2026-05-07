from re import *


with open(r'../files-24/24_9791.txt') as f:
    data = f.readline()

pattern = fr'[1-9A-F][0-9A-F]*'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
