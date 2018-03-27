t = int(raw_input())
for i in xrange(t):
	n = int(raw_input())
	f = int(raw_input())
	sum = f
	l = 0
	for j in xrange(n-1):
		a = map(int,raw_input().split())
		#print a
		n = max(a[l],a[l+1])
		l = a.index(n)
		sum += n
	print sum