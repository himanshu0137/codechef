n,q = map(int,raw_input().split())
a = map(int,raw_input().split())
mx = max(a)
mn = min(a)
while(q):
	t = int(raw_input())
	if(t <= mx and t >= mn):
		print "Yes"
	else:
		print "No"
	q -= 1