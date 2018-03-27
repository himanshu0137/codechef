from math import floor
n = 0
def profit(n):
	if floor(13*n/12) > n:
		a = profit(floor(n/2))
		b = profit(floor(n/3))
		c = profit(floor(n/4))
		return a+b+c
	else:
		return n
while 1:
	n = raw_input()
	if n != "":
		p = profit(int(n))
		print p
	else:
		break