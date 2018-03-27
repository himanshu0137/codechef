from sys import stdin,stdout
from math import floor
t = int(stdin.readline())
for _ in xrange(t):
	n = int(stdin.readline())
	a = floor((-1 + (1+8*n)**0.5)/2)
	stdout.write(str(a)[:-2])
	stdout.write('\n')