t = int(raw_input())
while(t):
	n,m,c = map(int,raw_input().split())
	s = min(n,m)
	l = max(n,m)
	count = 0
	for i in xrange(1,s+1):
		if c%i == 0 and c/i <= l:
			count += 1
	t -= 1
	print count