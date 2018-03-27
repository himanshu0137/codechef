from sys import stdin,stdout
t = int(stdin.readline())
for _ in xrange(t):
	n = int(stdin.readline())
	d = map(int,stdin.readline().split())
	mx = 0
	i = 2
	j = 0
	while i < n:
		m = 2
		for i in xrange(i,n):
			if d[i-2]+d[i-1] == d[i]:
				m += 1
			else:
				j = i
				break
		if mx < m:
			mx = m
			i += m
	stdout.write(str(m))
	stdout.write('\n')