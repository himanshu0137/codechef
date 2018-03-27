from sys import stdin,stdout
t = int(stdin.readline())
for _ in xrange(t):
	n = stdin.readline().strip()
	sm = 0
	for i in n:
		sm += int(i)
	stdout.write(str(sm)+"\n")