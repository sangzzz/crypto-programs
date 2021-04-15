import sys
from legendre_symbol import legendre_symbol
from jacobi_symbol import jacobi

def pepins_test(k, Fn):
    leg = legendre_symbol(k, Fn)
    jac = jacobi(k, Fn, verbose=False)
    print("Fn\t\t:\t{}".format(Fn))
    print("Legendre Symbol\t:\t{}".format(leg))
    print("Jacobi Symbol\t:\t{}".format(jac))
    if leg == jac:
        return True
    else:
        return False

if __name__ == "__main__":
    k, n = map(int, list(sys.argv)[1:])
    Fn = pow(2, pow(2, n)) + 1
    print()
    is_prime = pepins_test(k, Fn)
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")