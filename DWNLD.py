T = int(raw_input())
while T:
    n, k = map(int, raw_input().split())
    s = 0
    for i in xrange(n):
        t, d = map(int, raw_input().split())
        if k > 0:
            if k >= t:
                k -= t
            else:
                s += (t-k)*d
                k = 0
        else:
            s += t*d
    print s
    T -= 1
