from gcd import gcd
from multiplicative_inverse import inverse

if __name__ == "__main__":
    import sys
    p, q, m = list(map(int, list(sys.argv)[1:]))
    n = p * q
    phi_n = (p-1) * (q-1)
    d = None
    for i in range(int(phi_n/3), phi_n-1):
        if gcd(phi_n, i) == 1:
            d = i
            break
    if not d:
        print("Error in finding d")
    e = inverse(d, phi_n)
    print("\nPublic Key Pair\t\t:\t({}, {})".format(e, n))
    print("Private Key\t\t:\t{}".format(d))
    enc_m = pow(m, e, n)
    dec_m = pow(enc_m, d, n)
    print("Message\t\t\t:\t{}".format(m))
    print("Encrypted Message\t:\t{}".format(enc_m))
    print("Decrypted Message:\t:\t{}".format(dec_m))