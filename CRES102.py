def func(a, n):
    l = [0 for _ in xrange(n)]
    r = [0 for _ in xrange(n)]
    l[0] = a[0]
    r[n-1] = a[n-1]
    w = 0
    for i in xrange(1, n):
        l[i] = max(l[i-1], a[i])
    for i in xrange(n-2, -1, -1):
        r[i] = max(r[i+1], a[i])
    for i in xrange(n):
        w += (min(l[i], r[i]) - a[i])
    return w
def main():
    n = int(raw_input())
    a = map(int, raw_input().split())
    return func(a, n)
T = int(raw_input())
while T:
    print main()
    T -= 1
