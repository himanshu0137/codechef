t = int(raw_input())
def q(s,f):
	i = len(s)-1
	h = 0
	while i>=0:
		if s[i] == "1":
			h += 1
		else:
			if f:
				return h,False
		i -= 1
	if f:
		return h,True
	return h
while t:
	l1,l2,l3,n = map(list,raw_input().split())
	n = int(n[0])
	count = 1
	if l3[-1] == "1":
		w,k = q(l3,True)
		count -= w
		i = 0
		while(i < n):
			if k:
				w,k = q(l2,True)
				count -= w
			i += 1
		if k:
			w,k = q(l1,True)
			count -= w
	count += (q(l3,False)+q(l2,False)+q(l1,False))
	print count
	t -= 1