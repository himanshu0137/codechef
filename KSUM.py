from sys import stdin,stdout
n,k = map(int,stdin.readline().split())
a = map(int,stdin.readline().split())
def sa(a):
	q = 0
	for i in a:
		q += i
	return q
j = 0
l = []
p = 0
while p < k*(k+1)/2:
	s = 0
	for i in xrange(j+1):
		e = n-j+i
		if i == e:
			l.append(a[i])
		else:
			l.append(sa(a[i:e]))
		p += 1
	j += 1
print l
l = sorted(l)[::-1]
for i in l[:k]: stdout.write(str(i) + " ")