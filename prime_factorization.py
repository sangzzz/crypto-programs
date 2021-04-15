def prime_factorize(n):
    primes = []
    p = 2
    while p * p<= n :
        if n % p == 0 :
            count = 0
            while n % p == 0 :
                n = n // p
                count += 1
            if count > 0:
                primes.append((p, count))
        p = p + 1
    if n > 1 :
        primes.append((n, 1))
    return primes

import sys
if __name__ == "__main__":
    n = int(sys.argv[1])
    print("\nPrime Factorization of {}: {}".format(n, prime_factorize(n)))
