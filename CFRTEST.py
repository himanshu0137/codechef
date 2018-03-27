T = int(raw_input())
while T:
    n = int(raw_input())
    a = map(int, raw_input().split())
    d = [0 for _ in xrange(100)]
    for i in xrange(n):
        d[a[i]-1] += 1
        if d[a[i] - 1] > 1:
            n -= 1
    print n
    T -= 1
