t = int(raw_input())
for i in xrange(t):
	n,m = map(int,raw_input().split())
	dj = map(str,raw_input().split())
	c = list()
	ca = list()
	k = 0
	for j in xrange(1,n+1):
		if str(j) not in dj:
			if k%2 == 0:
				c.append(str(j))
			else:
				ca.append(str(j))
			k += 1
	if len(c) == 0:
		print " "
	else:
		print " ".join(c)
	if len(ca) == 0:
		print " "
	else:
		print " ".join(ca)