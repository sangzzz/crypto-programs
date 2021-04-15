from gcd import gcd
import sys

def lcm(x):
    ans = x[0]
    for i in x[1:]:
        ans = ans*i//gcd(ans,i)
    return ans

if __name__ == "__main__":
    nums = list(map(int, list(sys.argv)[1:]))
    print("LCM of {}: {}".format(nums, lcm(nums)))