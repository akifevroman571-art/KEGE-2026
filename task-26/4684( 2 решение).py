with open(r'files/26_4684.txt') as f:
    N = int(f.readline())
    tovar = [int(i) for i in f]
tovar = sorted(tovar)

sale = N // 6

