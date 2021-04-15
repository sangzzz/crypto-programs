from gcd import gcd
import sys

def group_function(x, n):
    return int(x**2 + 1)%n

def pollards_rho(x0, n):
    x_vals = [x0]
    for i in range(1, int(n**0.5)+2):
        x_vals.append(group_function(x_vals[-1], n))
        print("x{} : {}".format(i, x_vals[-1]))
        if i%2 == 0:
            d = gcd(abs(x_vals[i]-x_vals[i//2]), n)
            if d>1:
                print(d)
                break

if __name__ == "__main__":
    x0, n = map(int, list(sys.argv)[1:])
    pollards_rho(x0, n)