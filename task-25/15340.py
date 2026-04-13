from fnmatch import fnmatch
for n in range(1232202-1232202%2024, 10**10, 2024):
    if fnmatch(str(n),'1*2322?2'):
        print(n, n//2024)