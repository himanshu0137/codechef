T = int(raw_input())
while T:
    a = list(raw_input())
    b = list(raw_input())
    c = 0
    for i in xrange(len(a)):
        for j in xrange(len(b)):
            if a[i] == b[j]:
                c += 1
                b[j] = "0"
    print c
    T -= 1
