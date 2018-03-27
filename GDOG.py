t = int(raw_input())
while(t):
	n,k = map(int,raw_input().split())
	np = 1
	maxmod = 0
	for i in xrange(2,k+1):
		q = n%i
		if(q > maxmod):
			maxmod = q
			np = i-1
	print np
	t -= 1