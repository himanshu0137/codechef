T = int(raw_input())
while T:
    n, c, q = map(int, raw_input().split())
    for i in xrange(q):
        l, r = map(int, raw_input().split())
        if l <= c and c <= r:
            c = r + l -c
    print c
    T -= 1
