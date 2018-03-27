t = int(raw_input())
while t:
    n,k = map(int, raw_input().split())
    a = map(int, raw_input().split())
    ans = "even"
    if k <= 1:
        if (sum(a)+1)%2 == 1:
            ans = "odd"
    print ans
    t -= 1
    