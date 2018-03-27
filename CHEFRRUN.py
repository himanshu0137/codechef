from sys import stdin,stdout 
t = int(stdin.readline())
while(t):
	n = int(stdin.readline())
	circle = map(int,stdin.readline().split())
	count = 0
	for i in xrange(n):
		cur = i
		visited = [0]*n
		visited[cur] = 1
		while(1):
			cur = (cur+circle[cur]+1)%n
			if(cur == i):
				count += 1
				break
			if(visited[cur] == 0):
				visited[cur] = 1
			else:
				break
	stdout.write(str(count)+"\n")
	t -= 1
