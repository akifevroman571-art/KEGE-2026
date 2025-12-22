from string import printable as alp

for x in alp[:22]:
    num1 = int(f'A23{x}AC0', 22)
    num2 = int(f'GB{x}21670', 22)
    num = num1+num2
    if num % 21 ==0:
        print(num//22)