import sys
import random

def miller_rabin(p, security=10):
    if p == 2: 
        return True
    if not (p & 1):
        return False
    p1 = p - 1
    u = 0
    t = p1
    while t % 2 == 0:
        t >>= 1
        u += 1
    assert p-1 == 2**u * t
    
    def witness(a):
        z = pow(a, t, p)
        if z == 1:
            return False
        for i in range(u+1):
            z = pow(a, 2**i * t, p)
            if z == p1:
                return False
        print("Euler Witness\t:\t{}".format(a))
        for i in range(u+1):
            print("i = {}, z = {}".format(i, pow(a, 2**i * t, p)))
        return True

    for i in range(2,min(p, 20)):
        if witness(i):
            return False
    return True

if __name__ == "__main__":
    n = int(list(sys.argv)[1])
    print()
    is_prime = miller_rabin(n)
    if is_prime:
        print("Probably Prime")
    else:
        print("Not Prime")