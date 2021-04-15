from prime_factorization import prime_factorize
def phi(n):
    result = 1
    for prime_factor, power in prime_factorize(n):
        result = result * pow(prime_factor, power) * (prime_factor - 1) / prime_factor
    return int(result)

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1])
    print()
    print("Prime Factorization of {}: {}".format(n, prime_factorize(n)))
    print("Euler's Toitient of {}: {}".format(n, phi(n)))