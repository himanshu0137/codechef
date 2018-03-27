T = int(raw_input())
while T:
    G = int(raw_input())
    while G:
        I, N, Q = map(int, raw_input().split())
        I = I&1
        Q = Q&1
        if I^Q and N&1:
            print (N>>1) + 1
        else:
            print N>>1
        G -= 1
    T -= 1
