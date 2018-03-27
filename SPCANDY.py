T = int(raw_input())
while T:
    N, K = map(int, raw_input().split())
    print N//K, N%K
    T -= 1
