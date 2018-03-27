from sys import stdin,stdout
t = int(stdin.readline())
while(t):
	e = stdin.readline()
	stack = []
	for i in e:
		if(ord(i) <= 122 and ord(i) >= 97):
			stdout.write(i)
		elif(i == ")"):
			a = ""
			while(1):
				a = stack.pop()
				if(a=="("):
					break
				stdout.write(a)
		else:
			stack.append(i)
	stdout.write("\n")
	t -= 1