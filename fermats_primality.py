import sys

def fermats_primality(n, a):
    if pow(a,n-1,n) == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    args = list(sys.argv)[1:]
    print()
    print("Fermat's Primality: {}, {} --> {}".format(args[0], args[1], fermats_primality(int(args[0]), int(args[1]))))