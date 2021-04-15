import sys
import random
from gcd import gcd
from jacobi_symbol import jacobi

def solovay_strassen(n, security=10):
    candidates = []
    for i in range(security):
        a = random.randint(2, n-2)
        candidates.append(a)
        gcd_a_n = gcd(n, a)
        if gcd_a_n > 1:
            return False
        legendre = pow(a, (n-1)//2, n)
        if legendre == n - 1:
            legendre = -1
        jacobi_symbol = jacobi(a, n, verbose=False)
        if legendre != jacobi_symbol:
            print("Euler Liars\t:\t{}".format(candidates[:-1]))
            print("Euler Witness\t:\t{}".format(candidates[-1]))
            print("Legendre Symbol\t:\t{}".format(legendre))
            print("Jacobi Symbol\t:\t{}".format(jacobi_symbol))
            return False
    return True

if __name__ == "__main__":
    n = int(list(sys.argv)[1])
    print()
    is_prime = solovay_strassen(n)
    if is_prime:
        print("Probably Prime")
    else:
        print("Not Prime")