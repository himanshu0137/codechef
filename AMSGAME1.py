def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
def main():
    n = int(raw_input())
    a = map(int, raw_input().split())
    q = a[0]
    for i in xrange(1, n):
        q = gcd(q, a[i])
    return q
T = int(raw_input())
while T:
    print main()
    T -= 1
