T = int(input())
while T:
    LI = [0 for _ in range(100)]
    LF = [0 for _ in range(100)]
    SC = 0
    N, M = map(int, input().split())
    for i in range(N):
        c, l = map(int, input().split())
        LI[l-1] += c
    for i in range(M):
        c, l = map(int, input().split())
        LF[l-1] += c
    for i in range(100):
        if LI[i] < LF[i]:
            SC += LF[i]-LI[i]
    print(SC)
    T -= 1