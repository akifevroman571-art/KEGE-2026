with open(r'files/26_1868.txt') as f:
    N = int(f.readline())
    places = []
    for i in f:
        place = list(map(int, i.split()))
        places.append(place)
places = sorted(places, key=lambda x: (-x[0], x[1]))
ans = []
for i in range(len(places)-1):
    if places[i][0] == places[i+1][0]:
        if places[i+1][1] - places[i][1] ==3:
            print(places[i][0], places[i][1]+1)
            break










