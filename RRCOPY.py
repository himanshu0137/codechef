T = int(raw_input())
while T:
    c = [False for _ in xrange(100000)]
    l = 0
    n = int(raw_input())
    a = map(int, raw_input().split())
    for i in a:
        c[i-1] = True
    for i in c:
        if i:
            l += 1
    print l
    T -= 1
