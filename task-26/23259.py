with open('files/26_15_23259.txt') as f:
    N, M = map(int, f.readline().split())
    data = [int(i) for i in f]

data = sorted(data)
print(N, M)
print(data)
print(len(data))