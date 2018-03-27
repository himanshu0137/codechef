T = int(raw_input())
while T:
    n = int(raw_input())
    ans = float("inf")
    c = int(n**0.5)
    for i in xrange(1, c+1):
        if n%i == 0:
            ans = min(ans, abs(n/i-i))
    print ans
    T -= 1
