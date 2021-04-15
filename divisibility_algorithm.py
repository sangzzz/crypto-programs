import sys

coeffs = []
values = []

def gcd(a, b):
    global coeffs, values
    if b == 0:
        print("GCD:\t\t{}".format(a))
        return None
    coeffs.append(a//b)
    values.append(b)    
    gcd(b, a%b)

def divisibility(a, b):
    global coeffs, values
    values.append(max(a, b))
    a, b = max(a, b), min(a, b)
    gcd(a, b)

if __name__ == "__main__":
    args = list(map(int, list(sys.argv)[1:]))
    print()
    if len(args)>0:
        divisibility(int(args[0]), int(args[1]))
        print("Coefficients:\t{}\nValues:\t\t{}\n".format(coeffs, values))
    else:
        divisibility(42823, 6409)
        print("Coefficients:\t{}\nValues:\t\t{}\n".format(coeffs, values))