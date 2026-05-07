from string import printable

with open(r'../files-24/24_9791.txt') as f:
    data = ' '+f.readline().lower()+ ' '


for i in printable[12:36]:
    data = data.replace(i, ' ')

data = data.split()

ans = [len(i) for i in data if i[-1] in '02468A' and i[0] not in '0']
