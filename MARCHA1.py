"""
def func(a, n, m):
    if m == 0:
        return True
    if n == 0 and m != 0:
        return False
    if a[n-1] > m:
        func(a, n-1, m)
    return func(a, n-1, m) or func(a, n-1, m-a[n-1])
"""
def func(a, n, m):
    ss = [[False for _ in xrange(n+1)] for __ in xrange(m+1)]
    for i in xrange(n+1):
        ss[0][i] = True
    for i in xrange(1, m+1):
        ss[i][0] = False
    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            ss[i][j] = ss[i][j-1]
            if i >= a[j-1]:
                ss[i][j] = ss[i][j] or ss[i-a[j-1]][j-1]
    return ss[m][n]
def main():
    n, m = map(int, raw_input().split())
    a = []
    for _ in xrange(n):
        a.append(int(raw_input()))
    if func(a, n, m):
        return "Yes"
    return "No"
T = int(raw_input())
while T:
    print main()
    T -= 1
