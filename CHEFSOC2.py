from sys import stdin,stdout
t = int(stdin.readline())
ans = list()
def f(a,p,i,m,sr):
	print ans,i,p
	if i == m:
		global ans
		ans[p] += 1
		return 0
	else:
		if p-sr[i] >= 0:
			f(a,p-sr[i],i+1,m,st)
		if p+sr[i] < a:
			f(a,p+sr[i],i+1,m,st)
for _ in xrange(t):
	n,m,s = map(int,stdin.readline().strip().split(' '))
	st = map(int,stdin.readline().strip().split(' '))
	ans = [0]*n
	__ = f(n,s-1,0,m,st)
	ans = [i%1000000007 for i in ans]
	print ans