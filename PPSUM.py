t = int(raw_input())
while t:
	d,n = map(int,raw_input().split())
	for i in xrange(d):
		n = n*(n+1)/2
	print n
	t -= 1 