with open(r'files/26_17687.txt') as f:
    N = int(f.readline())
    goods = [int(i) for i in f]
goods = sorted(goods)[::-1]

prices_1 = sum(goods) - sum(goods[:N//9])
prices_2 = sum(goods) - sum(goods[8::9])
print(prices_1, prices_2)
