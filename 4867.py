for n in range(2, 1000000):
    R = f'{n:x}'
    sum_chet_chis = 0
    for i in str(n):
        if int(i) % 2 == 0:
            sum_chet_chis += int(i)

    sum_chet = sum(map(int, str(n)[1::2]))
    res = abs(sum_chet_chis -  sum_chet)
    if res == 9:
        print(n)
        break