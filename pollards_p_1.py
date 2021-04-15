from gcd import gcd
from lcm import lcm
import sys

def pminus1(n=491389):
    b = [i for i in range(5, n-1)]
    for B in b:
        k = lcm(list(range(1, B+1)))
        a_ = [i for i in range(2, n//10)]
        for a in a_:
            r = pow(a, k, n)
            d = gcd(n, r-1)
            if d!=1 and d!=n:
                print("\nn\t:\t{}".format(n))
                print("B\t:\t{}".format(B))
                print("k(LCM)\t:\t{}".format(k))
                print("a\t:\t{}".format(a))
                print("r\t:\t{}".format(r))
                print("d\t:\t{}".format(d))
                exit(0)

if __name__ == "__main__":
    n = int(list(sys.argv)[1])
    pminus1(n)