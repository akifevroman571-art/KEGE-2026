from string import printable as alph
ans = set()
for x in alph[:18]:
    for y in alph[max(9, int(x, 18)+1): 18]:
        num1 = int(f'5{x}{y}a', 18)
        num2 = int(f'18{x}7', int(y, 36))
        num = num1 + num2
        ans.add(num)
print(len(ans))
