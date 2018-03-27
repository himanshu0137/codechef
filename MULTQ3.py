n,q = map(int,raw_input().split())
array = [0]*n
while(q):
	c,a,b = map(int,raw_input().split())
	if(c):
		count = 0
		for i in xrange(a,b+1):
			if(array[i] == 0):
				count += 1
		print count
	else:
		for i in xrange(a,b+1):
			array[i] += 1
			array[i] %= 3
	q -= 1