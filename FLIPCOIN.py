n,q = map(int,raw_input().split())
l = [0]*n
for i in xrange(q):
	heads = 0
	c,a,b = map(int,raw_input().split())
	if c == 0:
		for j in xrange(a,b+1):
			l[j] ^= 1
	else:
		for j in xrange(a,b+1):
			heads += 1 if l[j] == 1 else 0
		print heads
	#print l
	#print 