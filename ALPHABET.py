s = [0]*26
q = raw_input()
for i in q:
	s[ord(i)-97] = 1
n = int(raw_input())
while(n):
	e = raw_input()
	f = 1
	for i in e:
		if not (s[ord(i)-97]):
			f = 0
			break
	if(f):
		print "Yes"
	else:
		print "No"
	n -= 1