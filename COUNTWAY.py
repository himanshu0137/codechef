memo = [0 for i in xrange(10001)]
def fact(q):
	if q == 1:
		return 1
	if memo[q] == 0:
		memo[q] = q*fact(q-1)
	return memo[q]
def main():
	n,k = map(int,raw_input().split())
	a = map(int,raw_input().split())
	d = dict()
	for i in a:
		d[i] = d.get(i,0)+1
	res = 1
	for i in xrange(n-k):
		res *= (n-i)
	for i in d:
		res /= fact(d[i])
	return res%13313
	
print main()