N = int(raw_input())
A = sum(map(int, raw_input().split()))
if A == N*(N+1)/2:
    print "YES"
else:
    print "NO"
