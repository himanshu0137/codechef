n = int(raw_input())
l = 0
w = 1
while(n):
	p1,p2 = map(int,raw_input().split())
	lead = p1-p2
	if(lead > 0 and lead > l):
		l = lead
		w = 1
	elif(lead < 0 and -lead > l):
		l = -lead
		w = 2
	n -= 1
	
print w,l