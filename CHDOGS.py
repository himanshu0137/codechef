import math
t = int(raw_input())
while t:
	t -= 1
	s,v = map(float,raw_input().split())
	r = (2*s)/(3*v)
	if r < 1e-6:
		r = math.ceil(r*1e7)/1e7
		print "%.7f" % r
		continue
	print "%.6f" % r