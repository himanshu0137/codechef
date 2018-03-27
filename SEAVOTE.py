t = int(raw_input())
for i in xrange(t):
	n = int(raw_input())
	l = map(int,raw_input().split())
	s = sum(l)
	if s>= 100 and s<=100+n:
		print "YES"
	else:
		print "NO"