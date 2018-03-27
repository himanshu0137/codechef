t = int(raw_input())
while t:
	d = raw_input()
	count0 = 0
	for i in d:
		if i == "0":
			count0 += 1
	count1 = len(d)-count0
	if count0 == 1 or count1 == 1:
		print "Yes"
	else:
		print "No"
	t -= 1