T = int(input())
while T:
    N = int(input())
    A = list(map(int, input().split()))
    S = 0
    W = [False for _ in range(N)]
    for i in range(N-1):
        if A[i]^A[i+1]:
            W[i], W[i+1] = True, True
    for i in range(N):
        if W[i]:
            S += 1
    print(S)
    T -= 1