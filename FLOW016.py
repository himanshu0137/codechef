def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x%y)
T = int(raw_input())
while T:
    a, b = map(int, raw_input().split())
    n = gcd(a, b)
    print "{} {}".format(n, a*b/n)
    T -= 1
