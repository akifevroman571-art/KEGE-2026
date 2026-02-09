from itertools import *
from string import printable
cnt = 0
for val in product(printable[:8], repeat=6):
    if val[0] != '0' and val.count('3') == 0