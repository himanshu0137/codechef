t = int(raw_input())
criminals = map(int,raw_input().split())
if t == 1:
	print "1"
else:
	ans = [0]*t
	for i in xrange(1,t):
		ans[criminals[i]-1] = 1
	res = ""
	for i in xrange(1,t):
		if ans[i] == 0:
			res += (str(i+1)+" ")
	print res