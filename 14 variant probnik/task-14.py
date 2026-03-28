from string import printable as alph
for x in alph[:43]:
    num1 = int('1b'+'x'+'af',43)
    num2 = int('f9'+'x'+'f4',43)
    num = num1+num2
    if num % 42==0:
        print(num//42)


