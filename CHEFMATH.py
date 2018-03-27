fib = [0,1]
def greedy(n):
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    i = 1
    while fib[i+1] <= n: i += 1
    digs = set()
    while n:
        while fib[i] > n: i -= 1
        digs.add(i)
        n -= fib[i]
    return digs

def F(n):
    digs = greedy(n)
    top = max(digs)
    dp = [[[0,0,0] for _ in xrange(4)] for _ in xrange(top+1)]
    for j in xrange(0, 2): dp[0][j][0] = 1
    for i in xrange(1, top + 1):
        for j in xrange(0,2):
            for k in xrange(0,j+1):
                if i in digs:
                    dp[i][j][k] = dp[i-1][k+j][j] + dp[i-1][k+j+1][j+1]
                else:
                    dp[i][j][k] = dp[i-1][k+j][j] + dp[i-1][k+j-1][j-1]
    return dp[top][0][0]
	
print F(12)