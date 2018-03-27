T = int(input())
while T:
    H, M = map(int, input().split())
    S = 1
    for i in range(1, 10):
        hc, mc, j, hf, mf, x = 0, 0, 0, True, True, i
        while hf or mf:
            if hf and x < H:
                hc += 1
            else:
                hf = False
            if mf and x < M:
                mc += 1
            else:
                mf = False
            x = x*10 + x
            j += 1
        S += hc*mc
    print(S)
    T -= 1