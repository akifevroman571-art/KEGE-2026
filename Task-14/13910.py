from string import printable
for p in range(int(max('TQNQU'), 36)+1, 37):
    n1 = int(f'TH', p)
    n2 = int(f'NQ', p)
    n3 = int(f'U', p)
    n4 = int(f'1L7', p)
    if n4 == n1+ n2+n3:
        print(p)
