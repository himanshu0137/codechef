def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
t = int(raw_input())
while t:
    n = int(raw_input())
    a = map(int,raw_input().split())
    cur = a[0]
    count = 0
    for i in xrange(1,n):
        x = gcd(cur,a[i])
        print i,cur,x,a[i]
        if(x > 1):
            count += 1
        else:
            cur = a[i]
    print count
    t -= 1