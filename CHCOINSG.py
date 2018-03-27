t = int(raw_input())
for _ in xrange(t):
	n = int(raw_input())
	turns = 0
	if(n == 1):
		print "Chef"
		continue
	while(n):
		turns += 1
		m = n
		factors = {}
		while(m%2 == 0):
			factors[2] = factors.get(2,0)+1
			m /= 2
		i = 3
		while(m != 1):
			while(m%i == 0):
				factors[i] = factors.get(i,0)+1
				m /= i
			i += 2
		options = [i**factors[i] for i in factors]
		n -= max(options)
	print "Chef" if turns%2 else "Misha"