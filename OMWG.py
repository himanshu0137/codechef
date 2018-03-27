t = int(raw_input())
while(t):
	n,m = map(int,raw_input().split())
	print 2*n*m - m - n
	t -= 1