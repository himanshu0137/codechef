t = int(raw_input())
while(t):
	ns = int(raw_input())
	tstacks = []
	g = 1
	c = 0
	while(c < ns):
		temp = map(int,raw_input().split())
		tstacks.append(temp[1:])
		c += 1
	order = map(int,raw_input().split())
	for i in order:
		f = 0
		for j in xrange(ns):
			if(len(tstacks[j])):
				if(i == tstacks[j][-1]):
					tstacks[j].pop()
					f = 1
					break
		if not f:
			print "No"
			g = 0
			break
	if(g):
		print "Yes"
	t -= 1