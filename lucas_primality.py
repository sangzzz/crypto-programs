from prime_factorization import prime_factorize
import sys
from fermats_primality import fermats_primality

def lucas_test(n, verbose=True):
    n_1 = n - 1
    prime_factors = prime_factorize(n_1)
    primes = [factor[0] for factor in prime_factors]
    reminders = {}
    correct_a = None
    reminders_for_each_a = {}
    for a in range(3, n_1):
        if not fermats_primality(n, a):
            continue
        reminders = {}
        flag = True
        for prime in primes:
            val = pow(a, n_1//prime, n)
            if val == 1:
                flag = False
            reminders[prime] = val
        reminders_for_each_a[a] = reminders
        if flag:
            correct_a = a
            break
    if verbose:
        print("n - 1\t\t:\t{}".format(n-1))
        print("Primes\t\t:\t{}".format(primes))
        print("Correct a\t:\t{}".format(correct_a))
        print("Reminders\t:\t{}".format(reminders))
        # print(reminders_for_each_a)

    if correct_a != None:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(list(sys.argv)[1])
    print()
    is_prime = lucas_test(n)
    if is_prime:
        print("\nPrime")
    else:
        print("\nNot Prime")