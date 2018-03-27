from sys import stdin,stdout
n = int(stdin.readline())
a = map(int,stdin.readline().split())
s = range(1,n+1)
for i in xrange(n):
	mx = 0
	m = 0
	for j in xrange(n):
		m = a[j]+s[j]
		if mx < m:
			mx = m
	for j in xrange(n-1):
		s[j],s[(j+1)%n] = s[(j+1)%n],s[j]
	stdout.write(str(mx))
	stdout.write(" ")