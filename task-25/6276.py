
from fnmatch import fnmatch

for N in range(1111 - 11111 % 2023, 10 ** 10 + 1, 141):
    if fnmatch(str(N), '1234*7'):
        print(N, N // 202)