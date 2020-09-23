import math
import sys


def add(a, b):
    return math.log10(10**float(a) * 10**float(b)) if a.isnumeric() and b.isnumeric() else None


if len(sys.argv) == 3:
    a = sys.argv[1]
    b = sys.argv[2]
    print(f"{a} + {b} = {res}\n") if (
        res := add(a, b)) else print('Input must only contain numbers\n')
else:
    print("Program needs 2 input argument\n")
