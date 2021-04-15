import sys

def gen_S(n):
    if n == 0:
        return 4
    Sn_1 = gen_S(n-1)
    print("S{} = {}".format(n-1, Sn_1))
    return Sn_1**2 - 2

def mersenne(n):
    Mn = 2**n - 1
    Sn_2 = gen_S(n-2)
    print("S{} = {}".format(n-2, Sn_2))
    print("M{} = {}".format(n, Mn))
    if Sn_2 % Mn == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    n = int(list(sys.argv)[1])
    print()
    is_prime = mersenne(n)
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")