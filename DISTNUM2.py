from sys import stdin,stdout
n,q = map(int,stdin.readline().strip().split(' '))
v = sorted(list(set(map(int,stdin.readline().strip().split(' ')))))
ans = 0
for i in xrange(n):
	a,b,c,d,k = map(int,stdin.readline().strip().split(' '))
	l = (a*max(ans,0)+b)%(n+1)-1
	r = (c*max(ans,0)+d)%(n+1)-1
	print l,r
	if l > r: l,r = r,l
	try:
		ans = v[l+k-1]
	except:
		ans = -1
	stdout.write(str(ans)+"\n")