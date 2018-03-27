t = int(raw_input())
while t:
    n = int(raw_input())
    a = map(int, raw_input().split())
    b = []
    a.sort()
    i = 0
    while i < n-1:
        if a[i] == a[i+1]:
            b.append(a[i])
            i += 1
        i += 1
    if len(b) < 2:
        print -1
    else:
        print b[0]*b[1]
    t -= 1
