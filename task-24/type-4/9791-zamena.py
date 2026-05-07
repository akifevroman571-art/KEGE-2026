from string import printable

with open(r'../files-24/24_9791.txt') as f:
    data = f.readline().lower()

for i in printable[16:36]:
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))






