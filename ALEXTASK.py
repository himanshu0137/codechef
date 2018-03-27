def gcd(q, w):
    if w == 0:
        return q
    return gcd(w, q%w)
def lcm(q, w):
    return q*w/gcd(q, w)
t = int(raw_input())
while t:
    n = int(raw_input())
    a = map(int, raw_input().split())
    mn = 1e18
    for i in xrange(n):
        for j in xrange(i+1, n):
            mn = min(mn, lcm(a[i], a[j]))
    print mn
    t -= 1
