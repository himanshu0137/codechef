from sys import stdin,stdout
s = str(stdin.readline())
sb = 0
k = 0
loc = 0
mx = 0
for n,i in enumerate(s):
	if i == '(':
		sb += 1
	elif i == ')':
		sb -= 1
	else:
		if sb > mx:
			loc = n
			mx = sb
#stdout.write(s.split('(')[-1].split(')')[0])
print mx,n
i = n
while s[i] != ')':
	print s[i]
	i += 1
stdout.write('\n')