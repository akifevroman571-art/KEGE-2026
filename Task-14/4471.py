a = 7*729**543 - 6*81**765 - 5*9**987-20
cnt = 0
while a:
    if a % 9 == 8:
        cnt +=1
    a //= 9
print(cnt)