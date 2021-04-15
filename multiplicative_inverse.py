import sys
from eulers_toitient import phi
def inverse(a, mod):
    if a == 1 or a == mod-1:
        return a
    return pow(a, phi(mod)-1, mod)

if __name__ == "__main__":
    a, mod = list(map(int, list(sys.argv)[1:]))
    print("Inverse of {} mod {}: {}".format(a, mod, inverse(a, mod)))