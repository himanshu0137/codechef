t = int(raw_input())
dq = -999
while(t):
	n,k = map(int,raw_input().split())
	a = map(int,raw_input().split())
	votes = [0]*n
	count = 0
	for i in xrange(n):
		if(i+1 == a[i]):
			votes[i] = dq
			continue
		votes[a[i]-1] += 1
	for i in votes:
		if(i>=k):
			count += 1
	print count
	t -= 1