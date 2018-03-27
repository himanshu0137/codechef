from sys import stdin,stdout
t = int(stdin.readline())
for _ in xrange(t):
	n,k = stdin.readline().strip().split(' ')
	laddu = 0
	for i in xrange(int(n)):
		a = stdin.readline().strip()
		if 'CONTEST_WON' in a:
			l = int(a.split(' ')[1])
			laddu += 300
			if l < 20:
				laddu += 20-l
		elif a == 'TOP_CONTRIBUTOR':
			laddu += 300
		elif 'BUG_FOUND' in a:
			l = int(a.split(' ')[1])
			if l >= 50:
				laddu += l
		elif a == 'CONTEST_HOSTED':
			laddu += 50
	print laddu
	if k == 'INDIAN':
		stdout.write(str(laddu//200))
	else:
		stdout.write(str(laddu//400))
	stdout.write("\n")