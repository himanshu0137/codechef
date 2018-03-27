T = int(raw_input())
while T:
    n = int(raw_input())
    x = map(int, raw_input().split())
    y = map(int, raw_input().split())
    if n&1:
        x.append(0)
        y.append(0)
        n = n+1
    xf = 0
    yf = 0
    for i in xrange(0, n, 2):
        xf = xf + x[i] + y[i+1]
        yf = yf + y[i] + x[i+1]
    print min(xf, yf)
    T -= 1
