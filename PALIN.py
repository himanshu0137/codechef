t = int(raw_input())
for i in xrange(t):
	n = int(raw_input())
	k = n+1
	while 1:
		if str(k) == str(k)[::-1]:
			print k
			break
		else:
			k += 1