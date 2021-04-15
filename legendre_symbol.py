import sys
from residue import kth_power_residue
def legendre_symbol(a, p):
    if a % p == 0:
        return 0
    leg = pow(a, (p-1)//2, p)
    if leg == p - 1:
        leg = -1
    return leg
    
def leg2(a, p):
    if a % p == 0:
        return 0
    else:
        residues, non_residues = kth_power_residue(2, p, verbose=False)
        if a in residues:
            return 1
        else:
            return -1

if __name__ == "__main__":
    a, p = map(int, list(sys.argv)[1:])
    print("\nLegendre Symbol: {}".format(leg2(a, p)))
    print("Legendre Symbol: {}".format(legendre_symbol(a,p)))