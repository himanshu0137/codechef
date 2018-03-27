from sys import stdin,stdout
t = int(stdin.readline())
def amazingness(a):
	s = []
	ans = 0
	for i in xrange(len(a)):
		val = 0
		for j in xrange(i,len(a)):
			val ^= int(a[j])
			if val not in s:
				ans += val
				s.append(val)
	return ans
for _ in xrange(t):
	l,r = map(int,stdin.readline().split(' '))
	sm = 0
	for i in xrange(l,r+1):
		sm += amazingness(str(i))
	stdout.write(str(sm)+"\n")