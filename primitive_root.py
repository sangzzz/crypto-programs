from eulers_toitient import phi
import sys
from gcd import gcd

def order(a, n):
    phi_n = phi(n)
    order = 1
    while a**order % n != 1:
        order += 1
    return order

def coprime(n):
    coprimes = []
    for i in range(1, n):
        if gcd(n, i) == 1:
            coprimes.append(i)
    return coprimes

def primitive_roots(n):
    roots = []
    phi_n = phi(n)
    if n == 2:
        return [1]
    elif n == 3:
        return [2]
    orders = {}
    for a in range(2, n-1):
        orders[a] = order(a, n)
        if orders[a] == phi_n:
            roots.append(a)
    assert len(roots) == phi(phi_n)
    return roots, orders

def reminder(g, n):
    reminders = []
    vals = [i for i in range(1, n)]
    for i in vals:
        reminders.append(pow(g, i, n))
    return vals, reminders

if __name__ == "__main__":
    n = int(list(sys.argv)[1])
    print("\nCoprime Numbers to {}: {}".format(phi(n), coprime(phi(n))))
    roots, orders = primitive_roots(n)
    print("Primitive Roots of {}: {}".format(n, roots))
    print("Orders of Numbers : {}".format(orders))
    root = roots[0]
    print("Root: ", root)
    indices, reminders = reminder(root, n)
    print("\nReminders for one primitive root: \n{}\n{}".format(indices, reminders))