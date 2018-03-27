T = int(raw_input())
while T:
    n, k = map(int, raw_input().split())
    a = map(int, raw_input().split())
    a.sort()
    s = sum(a)
    s1 = sum(a[:k])
    s2 = sum(a[n-k:])
    print max(abs(2*s1-s), abs(2*s2-s))
    T -= 1
