from decimal import *
t = int(raw_input())
for _ in xrange(t):
	k = int(raw_input())
	getcontext().prec = k+1
	print Decimal(103993)/Decimal(33102)