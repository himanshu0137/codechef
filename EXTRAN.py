T = int(raw_input())
while T:
    n = int(raw_input())
    a = map(int, raw_input().split())
    a.sort()
    def func():
        for i in xrange(n-1):
            if a[i] == a[i+1]:
                return a[i]
        if a[1] - a[0] != 1:
            return a[0]
        if a[n-1] - a[n-2] != 1:
            return a[n-1]
    print func()
    T -= 1
