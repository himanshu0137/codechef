from sys import stdin,stdout
t = int(stdin.readline())
for _ in xrange(t):
	n = stdin.readline().strip()
	stdout.write(str(int(n[0])+int(n[-1]))+"\n")