with open(r'files/26_17537.txt') as f:
    N, M, K = list(map(int, f.readline().split()))
    places = [list(map(int, i.split())) for i in f]
place = []
seats = [M] * (K+1)


for row, seat in places:
    seats[seat] = min(seats[seat], row-1)
for i in range(K):
    place.append([min(seats[i], seats[i+1]), i+1])
print(max(place))


