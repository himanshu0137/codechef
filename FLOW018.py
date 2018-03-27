from sys import stdin,stdout
t = int(stdin.readline())
for _ in xrange(t):
	n = int(stdin.readline())
	f = 1
	for i in xrange(1,n+1):
		f *= i
	stdout.write(str(f)+"\n")