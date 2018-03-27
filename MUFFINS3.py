from sys import stdin,stdout
from math import floor
t = int(stdin.readline())
for _ in xrange(t):
	n = int(stdin.readline())
	a = str(floor(n/2 + 1))[:-2] + "\n"
	stdout.write(a)