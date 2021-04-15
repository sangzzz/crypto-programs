import sys
if __name__ == "__main__":
    length = len(sys.argv)
    print()
    if length == 4:
        base, exponent, mod = list(map(int, list(sys.argv)[1:]))
        print(pow(base, exponent, mod))
    elif length == 5:
        multiply, base, exponent, mod = list(map(int, list(sys.argv)[1:]))
        print("PowMod: {}".format(pow(base, exponent, mod)))
        print("MultiplyPowMod: {}".format(multiply*pow(base, exponent, mod)))
        print("MultiplyPowModMod: {}".format(multiply*pow(base, exponent, mod)%mod))
    else:
        print("Wrong Command Line Input")