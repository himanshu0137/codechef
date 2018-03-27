from math import floor
t = int(raw_input())
for i in xrange(t):
	b = int(raw_input())
	ans = 0
	n = 2
	while n<b:
		y = (b-n)/2
		if y>0:
			ans += floor(y)
		else:
			break
		n += 2
	print str(ans).split('.')[0]