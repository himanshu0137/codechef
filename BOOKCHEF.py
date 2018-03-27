n,m = map(int,raw_input().split())
special = map(int,raw_input().split())
posts = [[] for i in xrange(m)]
for i in xrange(m):
	a,b,c = raw_input().split()
	posts[int(a)-1] = [int(b),c,0]
	if int(a) in special:
		posts[int(a)-1][2] = 1
	
for i in xrange(m):
	for j in xrange(i+1,m):
		if posts[j][2] > posts[i][2]:
			posts[j],posts[i] = posts[i],posts[j]
		elif posts[j][2] == posts[i][2]:
			if posts[j][0] > posts[i][0]:
				posts[j],posts[i] = posts[i],posts[j]

for i in posts:
	print i[1]