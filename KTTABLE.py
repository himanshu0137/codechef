t = int(raw_input())
while(t):
	n = int(raw_input())
	a = [0]
	a += map(int,raw_input().split())
	b = map(int,raw_input().split())
	count = 0
	for i in xrange(n):
		if(b[i] <= a[i+1]-a[i]):
			count += 1
	print count
	t -= 1