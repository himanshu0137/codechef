"""def coord(a,n):
	for q,i in enumerate(a):
		if n in i:
			return q,i.index(n)"""

import numpy as np			
t = int(raw_input())
for i in xrange(t):
	n = int(raw_input())
	a = list()
	step = 0
	for j in xrange(n):
		a.append(map(int,raw_input().split()))
	for j in xrange(1,n*n):
		x1,y1 = [pos for pos, x in np.ndenumerate(np.array(a)) if x == j][0]
		x2,y2 = [pos for pos, x in np.ndenumerate(np.array(a)) if x == j+1][0]
		step += abs(x2-x1) + abs(y2-y1)
	print step