from sys import stdin,stdout
t = int(stdin.readline())
for _ in xrange(t):
	n = int(stdin.readline())
	l = [[]]
	for j in xrange(n):
		a = str(stdin.readline().strip()).replace(' ','')
		f = 0
		for i in l:
			if a not in i:
				i.append(a)
				f = 0
				break
			else:
				f = 1
		if f:
			l.append([a])
	stdout.write(str(len(l)))
	stdout.write('\n')