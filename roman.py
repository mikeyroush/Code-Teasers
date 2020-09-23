import sys


class Roman:

    romanDict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    @classmethod
    def toInt(cls, string):
        try:
            chars = [cls.romanDict[x] for x in string.upper()]
        except:
            return

        val = 0
        for i in range(len(chars)):
            if i > 0 and chars[i] > chars[i-1]:
                val += chars[i] - 2 * chars[i-1]
            else:
                val += chars[i]
        return val


if len(sys.argv) == 2:
    print(f"{sys.argv[1]}: {res}\n") if (
        res := Roman.toInt(sys.argv[1])) else print('String must only contain roman numerals\n')
else:
    print("Program needs 1 input argument\n")
