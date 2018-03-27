t = int(raw_input())
while t:
	l1,l2,l3,n = map(list,raw_input().split())
	n = int(n[0])
	a = ["0"]+l1+l2*n+l3
	count = 0
	g = len(l1)+len(l2)*n+len(l3)
	while 1:
		if a[g] == "1":
			a[g] = "0"
			g -= 1
		else:
			a[g] = "1"
			break
	for i in a:
		if i == "1":
			count += 1
	print count
	t -= 1