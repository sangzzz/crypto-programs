import sys
from gcd import gcd
def jacobi(a, n, verbose=True):
    if gcd(a, n) > 1:
        print("GCD: {}".format(gcd(a, n)))
        return 0
    if a>n:
        a = a%n
        if verbose:
            print("\t\t\t({} / {})".format(a, n))
    if a == 1 or a == -1:
        return a
    elif a % 2 == 0:
        if verbose:
            print("(2/{})={}, \t\t({} / {})".format(n, pow(-1, (n*n - 1)//8), a//2, n))
        return jacobi(a//2, n, verbose=verbose) * pow(-1, (n*n - 1)//8)
    else:
        if verbose:
            print("{}, \t\t\t({} / {})".format(pow(-1, ((a-1)//2) * ((n-1)//2)), n, a))
        return jacobi(n, a, verbose=verbose) * pow(-1, ((a-1)//2) * ((n-1)//2))

if __name__ == "__main__":
    a, n = map(int, list(sys.argv)[1:])
    print("\nJacobi Symbol of {} and {}: {}".format(a, n, jacobi(a, n)))

