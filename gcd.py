def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    return gcd(b, a%b)

import sys
if __name__ == "__main__":
    args = list(map(int, list(sys.argv)[1:]))
    print("\nGCD of {} and {}: {}".format(args[0], args[1], gcd(args[0], args[1])))