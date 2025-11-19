cnt = 0

for n in range(10, 40):
    R = f'{n:b}'
    if R[-4:] == 1011:
        R = int(R, 2)
    print(R)
print(int('11011', 2))





