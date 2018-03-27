t = int(raw_input())
while(t):
	n,m = map(int,raw_input().split())
	girls = [0]*m
	col = 0
	while(n):
		s=raw_input()
		for i in xrange(m):
			if(s[i]=='1'):
				girls[i] += 1
		n -= 1
	for i in xrange(m):
		col += girls[i]*(girls[i]-1)/2
	print col
	t -= 1