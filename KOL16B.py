T = int(raw_input())
for t in xrange(T):
    N = int(raw_input())
    I = []
    A = []
    B = []
    for _ in xrange(N):
        I.append(int(raw_input()))
    for j in xrange(N):
        A.append(I[j]>>16)
        B.append(I[j]&65535)
    print "Case {}:".format(t+1)
    print " ".join(map(str, B))
    print " ".join(map(str, A))
