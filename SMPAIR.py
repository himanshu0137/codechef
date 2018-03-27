T = int(raw_input())
while T:
    n = int(raw_input())
    a = map(int, raw_input().split())
    a.sort()
    print a[0]+a[1]
    T -= 1
