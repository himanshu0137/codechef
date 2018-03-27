def aton(a):
	return ord(a)-97
def mod(n):
	if n < 0:
		return 26+n
	else:
		return n
t = int(raw_input())
for _ in xrange(t):
	s = str(raw_input())
	l = len(s)
	steps = 1+l
	for n in xrange(l-1):
		steps += mod(aton(s[n+1])-aton(s[n]))
	if steps < 11*l:
		print "YES"
	else:
		print "NO"