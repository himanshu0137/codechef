T = int(raw_input())
while T:
    n = int(raw_input())
    a = map(int, raw_input().split())
    lp = -1
    lf = 0
    for i in xrange(n):
        if a[i] == 0:
            if lp < 0:
                lp += i
            lf += 1
    print lf*1000 + lp*100
    T -= 1
