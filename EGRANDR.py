t = int(raw_input())
def check():
	f = False
	sum = 0
	for i in xrange(n):
		if(a[i] <= 2):
			return False
		if(a[i] == 5):
			f = True
		sum += a[i]
	if(f):
		if(sum/n >= 4):
			return True
	return False
while(t):
	n = int(raw_input())
	a = map(int,raw_input().split())
	if(check()):
		print "Yes"
	else:
		print "No"
	t -= 1
	