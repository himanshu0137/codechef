from sys import stdin,stdout
t = int(stdin.readline())
for _ in xrange(t):
	n,k = map(int,stdin.readline().split())
	d = map(int,stdin.readline().split())
	q = map(int,stdin.readline().split())
	i = 0
	m = 0
	while i < n-k:
		j = 0
		f = 0
		for a in q:
			if d[i+j+1]-d[i+j] == a:
				f = 1
				j += 1
			else:
				f = 0
				break
		if f:
			m += 1
			i += k
		else:
			i += 1
	stdout.write(str(m))
	stdout.write('\n')