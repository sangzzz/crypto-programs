import sys

def kth_power_residue(k, n, verbose=True):
    residues = set()
    steps = []
    for i in range(1, n):
        residues.add(pow(i, k, n))
        steps.append(pow(i, k, n))
    if verbose:
        print("\nSteps a\t\t\t\t: {}".format([i for i in range(1, n)]))
        print("Steps a^2 (mod {})\t\t: {}".format(n, steps))
    return list(residues), [i for i in range(1, n) if i not in list(residues)]

if __name__ == "__main__":
    k, n = map(int, list(sys.argv)[1:])
    residues, non_residues = kth_power_residue(k, n)
    print("{}-Power Residues of {}\t\t: {}".format(k, n, residues))
    print("{}-Power Non-Residues of {}\t: {}".format(k, n, non_residues))
